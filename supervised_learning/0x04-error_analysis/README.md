# 0x04-error_analysis

## 0. Create Confusion
Write the function def create_confusion_matrix(labels, logits): that creates a confusion matrix:

- labels is a one-hot numpy.ndarray of shape (m, classes) containing the correct labels for each data point
    - m is the number of data points
    - classes is the number of classes
- logits is a one-hot numpy.ndarray of shape (m, classes) containing the predicted labels
- Returns: a confusion numpy.ndarray of shape (classes, classes) with row indices representing the correct labels and column indices representing the predicted labels**

## 1. Sensitivity
Write the function def sensitivity(confusion): that calculates the sensitivity for each class in a confusion matrix:

- confusion is a confusion numpy.ndarray of shape (classes, classes) where row indices represent the correct labels and column indices represent the predicted labels
    - classes is the number of classes
- Returns: a numpy.ndarray of shape (classes,) containing the sensitivity of each class

## 2. Precision
Write the function def precision(confusion): that calculates the precision for each class in a confusion matrix:

- confusion is a confusion numpy.ndarray of shape (classes, classes) where row indices represent the correct labels and column indices represent the predicted labels
    - classes is the number of classes
- Returns: a numpy.ndarray of shape (classes,) containing the precision of each class

## 3. Specificity
Write the function def specificity(confusion): that calculates the specificity for each class in a confusion matrix:

- confusion is a confusion numpy.ndarray of shape (classes, classes) where row indices represent the correct labels and column indices represent the predicted labels
    - classes is the number of classes
- Returns: a numpy.ndarray of shape (classes,) containing the specificity of each class

## 4. F1 score
Write the function def f1_score(confusion): that calculates the F1 score of a confusion matrix:

- confusion is a confusion numpy.ndarray of shape (classes, classes) where row indices represent the correct labels and column indices represent the predicted labels
    - classes is the number of classes
- Returns: a numpy.ndarray of shape (classes,) containing the F1 score of each class

## 5. Dealing with Error
Answer the question of how you should approach the following scenarios.

Scenarios:

    1. High Bias, High Variance
    2. High Bias, Low Variance
    3. Low Bias, High Variance
    4. Low Bias, Low Variance

Approaches:

    A. Train more
    B. Try a different architecture
    C. Get more data
    D. Build a deeper network
    E. Use regularization
    F. Nothing