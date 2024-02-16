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

            boxes.append(output[:, :, :, 0:4])
            box_confidences.append(self.sigmoid(output[:, :, :, 4:5]))
            box_class_probs.append(self.sigmoid(output[:, :, :, 5:]))

            t_x = output[:, :, :, 0]
            t_y = output[:, :, :, 1]
            t_w = output[:, :, :, 2]
            t_h = output[:, :, :, 3]
            c_x = np.indices((grid_height, grid_width, anchor_boxes))[1]
            c_y = np.indices((grid_height, grid_width, anchor_boxes))[0]
            b_x = self.sigmoid(t_x) + c_x
            b_y = self.sigmoid(t_y) + c_y
            # normalization to have b_x and b_y by grid
            b_x /= grid_width
            b_y /= grid_height

            p_w = self.anchors[i, :, 0]
            p_h = self.anchors[i, :, 1]
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

            boxes[i][:, :, :, 0] = x1
            boxes[i][:, :, :, 1] = y1
            boxes[i][:, :, :, 2] = x2
            boxes[i][:, :, :, 3] = y2

        return boxes, box_confidences, box_class_probs
