#!/usr/bin/env python3
"""
module containing class Yolo:
Class constructor: def __init__(self, model_path, classes_path, class_t,
                                nms_t, anchors)
Public instance attributes: model, class_names, class_t, nms_t, anchors
"""
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
