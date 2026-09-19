# Task 1: Building an Image Classification Model using CNN

### Objective:

To develop a Convolutional Neural Network (CNN) for image classification and understand the complete workflow of training, validating, and saving a deep learning model.

### Deliverables:

- Jupyter Notebook/Python Script.
  - [Code file](LNT_TASK_1.ipynb)
- Saved CNN model file.
  - [Models](https://github.com/persianflower/Deep-Learning/tree/main/LNT_Task_1/saved_model)
- Accuracy and loss curves.
  ![Curve](https://github.com/persianflower/Deep-Learning/blob/main/LNT_Task_1/outputs/acc%20%26%20loss%20curve.png)
- Performance evaluation report
  
  - Model Comparision
   ![Model comparision](https://github.com/persianflower/Deep-Learning/blob/main/LNT_Task_1/outputs/model%20comparision.png)

  - Confusion Matrix
     ![Confusion matrix](https://github.com/persianflower/Deep-Learning/blob/main/LNT_Task_1/outputs/confusion%20matric.png)
    
  - Basic CNN predictions
    ![Basic CNN predictions](https://github.com/persianflower/Deep-Learning/blob/main/LNT_Task_1/outputs/cnn%20predictions.png)


### Project Summary and Conclusion

This project successfully implemented and compared two different deep learning models (Basic CNN, and Deeper CNN) for classifying images from the Fashion-MNIST dataset.

**Summary of Work:**

1.  **Data Preparation:** The Fashion-MNIST dataset was loaded, normalized, reshaped, and one-hot encoded, preparing it for use with the different model architectures.
2.  **Model Development:** Two models of increasing complexity were defined: a basic Convolutional Neural Network (CNN), and a deeper CNN with additional layers, batch normalization, and dropout.
3.  **Model Training:** Each model was trained using the preprocessed training data with Early Stopping and Model Checkpointing to prevent overfitting and save the best performing weights based on validation loss. It also applied optimization metrics.
4.  **Model Evaluation:** The trained models were evaluated on the test set. Performance metrics (loss and accuracy) were calculated, and the training history was visualized. Confusion matrices were generated to analyze class-specific performance.
5.  **Prediction Analysis:** Predictions were made using the Basic CNN model, and examples of correctly and incorrectly classified images were visualized to gain insights into the model's strengths and weaknesses.

**Key Findings and Conclusion:**

Based on the evaluation results:

*   The **Basic CNN model** generally achieved the best balance of performance (highest accuracy, lowest loss) on the test set compared to the Deeper CNN model.
*   The **Deeper CNN model**, despite its increased complexity, did not consistently outperform the Basic CNN model on this dataset. This could be due to various factors such as the dataset size, the architecture choices, or the regularization applied. For this particular task and dataset, the increased complexity of the deeper model might not have been necessary or could have led to some overfitting despite the regularization techniques.

In conclusion, the Basic CNN model demonstrated superior performance for this Fashion-MNIST classification task, suggesting that a moderate level of complexity with convolutional layers is effective for this dataset. Further tuning of hyperparameters or architectural variations might potentially improve performance across all models, but the current results clearly show the benefits of CNNs over deeper CNNs for image data.

