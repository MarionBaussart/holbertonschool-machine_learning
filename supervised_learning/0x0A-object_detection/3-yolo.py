#!/usr/bin/env python3
"""
module containing class Yolo:
Class constructor: def __init__(self, model_path, classes_path, class_t,
                                nms_t, anchors)
Public instance attributes: model, class_names, class_t, nms_t, anchors
Public method: def process_outputs(self, outputs, image_size)
"""
import numpy as np
import tensorflow.keras as K


class Yolo:
    """
    Class Yolo : uses the Yolo v3 algorithm to perform object detection
    """

    def __init__(self, model_path, classes_path, class_t, nms_t, anchors):
        """
        Class contructor
        Args:
            model_path:  path to where a Darknet Keras model is stored
            classes_path: path to where the list of class names used for the
                Darknet model, listed in order of index, can be found
            class_t: float representing the box score threshold for the initial
                filtering step
            nms_t: float representing the IOU threshold for non-max suppression
            anchors: numpy.ndarray of shape (outputs, anchor_boxes, 2)
                containing all of the anchor boxes:
                    outputs: number of outputs (predictions) made by the
                        Darknet model
                    anchor_boxes is the number of anchor boxes used for each
                        prediction
                    2 => [anchor_box_width, anchor_box_height]
        Public instance attributes:
            model: the Darknet Keras model
            class_names: a list of the class names for the model
            class_t: the box score threshold for the initial filtering step
            nms_t: the IOU threshold for non-max suppression
            anchors: the anchor boxes
        """
        self.model = K.models.load_model(model_path)

        with open(classes_path, "r") as classes_file:
            self.class_names = []
            for class_name in classes_file:
                self.class_names.append(class_name.strip())

        self.class_t = class_t
        self.nms_t = nms_t
        self.anchors = anchors

    def sigmoid(self, x):
        """Sigmoïd function : 1 / (1 + e^(-x))"""
        sigmoid = 1 / (1 + np.exp(-x))
        return sigmoid

    def process_outputs(self, outputs, image_size):
        """
        Public method that preprocess outputs
        Args:
            outputs: list of numpy.ndarrays containing the predictions from the
                Darknet model for a single image.
                Output shape:
                    (grid_height, grid_width, anchor_boxes, 4 + 1 + classes)
            image_size: numpy.ndarray containing the image's original size
                [image_height, image_width]
        Return:
            Tuple of (boxes, box_confidences, box_class_probs)
                boxes: a list of numpy.ndarrays of shape
                    (grid_height, grid_width, anchor_boxes, 4)
                    containing the processed boundary boxes for each output
                box_confidences: a list of numpy.ndarrays of shape
                    (grid_height, grid_width, anchor_boxes, 1)
                    containing the box confidences for each output
                box_class_probs: a list of numpy.ndarrays of shape
                    (grid_height, grid_width, anchor_boxes, classes)
                    containing the box's class probabilities for each output
        """
        boxes = []
        box_confidences = []
        box_class_probs = []
        image_height, image_width = image_size

        for i, output in enumerate(outputs):
            grid_height = output.shape[0]
            grid_width = output.shape[1]
            anchor_boxes = output.shape[2]
            classes = output.shape[3] - 5

            boxes.append(np.zeros(shape=(grid_height,
                                         grid_width,
                                         anchor_boxes,
                                         4)))
            box_confidences.append(np.zeros(shape=(grid_height,
                                                   grid_width,
                                                   anchor_boxes,
                                                   1)))
            box_class_probs.append(np.zeros(shape=(grid_height,
                                                   grid_width,
                                                   anchor_boxes,
                                                   classes)))

            for h in range(grid_height):
                for w in range(grid_width):
                    for anchor in range(anchor_boxes):
                        t_x = output[h][w][anchor][0]
                        t_y = output[h][w][anchor][1]
                        t_w = output[h][w][anchor][2]
                        t_h = output[h][w][anchor][3]

                        c_x = h
                        c_y = w
                        b_x = self.sigmoid(t_x) + c_x
                        b_y = self.sigmoid(t_y) + c_y
                        # normalization to have b_x and b_y by grid
                        b_x /= grid_width
                        b_y /= grid_height

                        p_w = self.anchors[i][anchor][0]
                        p_h = self.anchors[i][anchor][1]
                        input_width = self.model.input.shape[1]
                        input_height = self.model.input.shape[2]
                        b_w = p_w * np.exp(t_w)
                        b_h = p_h * np.exp(t_h)
                        # normalization by input of darknet model
                        b_w /= input_width
                        b_h /= input_height

                        x1 = (b_x - (b_w / 2)) * image_width
                        y1 = (b_y - (b_h / 2)) * image_height
                        x2 = (b_x + (b_w / 2)) * image_width
                        y2 = (b_y + (b_h / 2)) * image_height

                        boxes[i][h][w][anchor] = x1, y1, x2, y2

                        box_confidence = self.sigmoid(output[h][w][anchor][4])
                        box_confidences[i][h][w][anchor] = box_confidence

                        classes = self.sigmoid(output[h][w][anchor][5:])
                        box_class_probs[i][h][w][anchor] = classes

        return boxes, box_confidences, box_class_probs

    def filter_boxes(self, boxes, box_confidences, box_class_probs):
        """
        Public method that give us information about bounding boxes
        Args:
            boxes: numpy.ndarrays of shape
                (grid_height, grid_width, anchor_boxes, 4)
                containing the processed boundary boxes for each output.
            box_confidences: numpy.ndarrays of shape
                (grid_height, grid_width, anchor_boxes, 1)
                containing the processed box confidences for each output.
            box_class_probs: numpy.ndarrays of shape
                (grid_height, grid_width, anchor_boxes, classes)
                containing the processed box class probabilities for each
                output.
        Return:
            Tuple of (filtered_boxes, box_classes, box_scores)
                filtered_boxes: numpy.ndarray of shape (?, 4)
                    containing all of the filtered bounding boxes
                box_classes: numpy.ndarray of shape (?,)
                    containing the class number that each box in filtered_boxes
                    predicts
                box_scores: numpy.ndarray of shape (?)
                    containing the box scores for each box in filtered_boxes
        """
        filtered_boxes = []
        box_classes = []
        box_scores = []

        grid_height = box_class_probs[0].shape[0]
        grid_width = box_class_probs[0].shape[1]
        anchor_boxes = box_class_probs[0].shape[2]
        classes = box_class_probs[0].shape[3]

        for i in range(len(boxes)):
            for h in range(grid_height):
                for w in range(grid_width):
                    for anchor in range(anchor_boxes):
                        # get the box_score = box_confidence * class_prob
                        box_conf = box_confidences[i][h][w][anchor][0]
                        scores = []
                        for num_classe in range(classes):
                            class_prob = box_class_probs[
                                i][h][w][anchor][num_classe]
                            box_score = box_conf * class_prob
                            scores.append(box_score)

                        if max(scores) >= self.class_t:
                            filtered_boxes.append(boxes[i][h][w][anchor])
                            index_max = scores.index(max(scores))
                            box_classes.append(index_max)
                            class_prob = box_class_probs[
                                i][h][w][anchor][index_max]
                            box_score = box_conf * class_prob
                            box_scores.append(box_score)

            np_filtered_boxes = np.asarray(filtered_boxes)
            np_box_classes = np.asarray(box_classes)
            np_box_scores = np.asarray(box_scores)

            return np_filtered_boxes, np_box_classes, np_box_scores
