
# Task 2: Transfer Learning using VGG16/ResNet

### Objective:

To implement transfer learning using pre-trained deep learning models and analyze performance improvements over custom CNN architectures.
### Deliverables:

- Jupyter Notebook/Python Script.
  - [Code file](LNT_TASK_2.ipynb)
- Accuracy and loss visualizations.
  - RESNET 50
    
  ![Accuracy](LNT_Task_2/outputs/resnet_acc.png)
  
  ![Loss](LNT_Task_2/outputs/resnet_loss.png)

  - CNN

  ![Accuracy](LNT_Task_2/outputs/cnn_acc.png)
  
  ![Loss](LNT_Task_2/outputs/cnn_loss.png)
  
- Performance comparision report

The aim of this assignment was to compare the results of a basic CNN to that of a transfer learning RESNET 50 model. When the accuracy of both were compared the basic CNN model shows a lot higher accurcy (approximately 50% greater) then that of RESNET. 

When their training time is compared the RESNET model (14 m/s) being finetuned takes longer time compared to CNN (11 m/s) as well. While the accuracy of RESNET over validation does increase over time the loss also increases exponentially. Comparatively the accuracy of CNN increases while its loss decreases after a sharp increase.

This could have varied reasons. When evaluating the model fitting epochs we come to the conclusion that the RESNET 50 model was overfitted which could be observed via the high accuracy of training (~90%) compared to that of the validation accuracy (approximately 45%) which is directly half of the other. The reason behind this could be a small dataset or that we should have finetuned more layers.

Compared to that the CNN model performed exceptionally in both training as well as validation phase with a high accuracy in both. When compared the CNN model should be selected for the classification task.


### Project Summary and Conclusion

This project successfully implemented and compared two different deep learning models (Basic CNN, and RESNET 50) for classifying images from the CIFAR-100 dataset.

**Summary of Work:**

1. Data Loading and Preprocessing: Loaded the CIFAR-100 dataset and preprocessed images using model-specific functions.
2. Model Adaptation: Loaded pre-trained ResNet50 added new classification layers for 100 classes, and initially froze base model layers.
3. Model Training: Defined layers for the basic CNN model.
4. Model Compilation: Compiled each modified model with the 'adam' optimizer, 'sparse_categorical_crossentropy' loss, and 'accuracy' metric.
5. Fine-Tuning: Demonstrated fine-tuning by unfreezing top layers of the ResNet50 model and training it for 30 epochs.
6. Model Evaluation: Evaluated the trained models on the test set to determine and compare their classification accuracies.

**Key Findings and Conclusion:**

Based on the evaluation results:

*   The **Basic CNN model** generally achieved the best balance of performance (highest accuracy, lowest loss) on the test set compared to the RESNET 50.
*   The **RESNET 50 model**, despite its increased complexity, and ability to fine tune pretrained model it did not consistently outperform the Basic CNN model on this dataset. This could be due to various factors such as the dataset size, the architecture choices, or the regularization applied. For this particular task and dataset, the increased complexity of the RESNET 50 might not have been necessary or could have led to some overfitting despite the regularization techniques.

In conclusion, the Basic CNN model demonstrated superior performance for this classification task, suggesting that a moderate level of complexity with convolutional layers is effective for this dataset. Further tuning of hyperparameters or architectural variations might potentially improve performance across all models, but the current results clearly show the benefits of CNNs over RESNET 50 for image data.

