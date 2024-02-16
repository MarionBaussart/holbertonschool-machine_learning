# 0x0C-neural_style_transfer

## 0. Initialize
Create a class NST that performs tasks for neural style transfer:

- Public class attributes:
    - style_layers = ['block1_conv1', 'block2_conv1', 'block3_conv1', 'block4_conv1', 'block5_conv1']
    - content_layer = 'block5_conv2'
- Class constructor: def __init__(self, style_image, content_image, alpha=1e4, beta=1):
    - style_image - the image used as a style reference, stored as a numpy.ndarray
    - content_image - the image used as a content reference, stored as a numpy.ndarray
    - alpha - the weight for content cost
    - beta - the weight for style cost
    - if style_image is not a np.ndarray with the shape (h, w, 3), raise a TypeError with the message style_image must be a numpy.ndarray with shape (h, w, 3)
    - if content_image is not a np.ndarray with the shape (h, w, 3), raise a TypeError with the message content_image must be a numpy.ndarray with shape (h, w, 3)
    - if alpha is not a non-negative number, raise a TypeError with the message alpha must be a non-negative number
    - if beta is not a non-negative number, raise a TypeError with the message beta must be a non-negative number
    - Sets Tensorflow to execute eagerly
    - Sets the instance attributes:
        - style_image - the preprocessed style image
        - content_image - the preprocessed content image
        - alpha - the weight for content cost
        - beta - the weight for style cost
- Static Method: def scale_image(image): that rescales an image such that its pixels values are between 0 and 1 and its largest side is 512 pixels
    - image - a numpy.ndarray of shape (h, w, 3) containing the image to be scaled
    - if image is not a np.ndarray with the shape (h, w, 3), raise a TypeError with the message image must be a numpy.ndarray with shape (h, w, 3)
    - The scaled image should be a tf.tensor with the shape (1, h_new, w_new, 3) where max(h_new, w_new) == 512 and min(h_new, w_new) is scaled proportionately
    - The image should be resized using bicubic interpolation
    - After resizing, the image’s pixel values should be rescaled from the range [0, 255] to [0, 1].
    - Returns: the scaled image
