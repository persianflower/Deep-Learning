# Task 5: API Testing and Validation using Postman/Curl

### Objective

To validate and test deep learning prediction APIs using industry-standard testing tools.

### Deliverables

- Postman Collection.

[Exported Collection](https://github.com/persianflower/Deep-Learning/blob/main/LNT_Task_5/Flask%20API%20Testing.postman_collection.json)

- API testing report.

API testing was carried out on the Flask API file created in [Task 4](https://github.com/persianflower/LNT_Task_4/blob/main/main.py). On the initial code various errors were discovered which were occurring due to using json format in response, this was then changed in order to be able to carry out predictions. Instead, file format was chosen to be
taken. This ensured that the image could be taken as well as initial preprocessing of it could be carried out. 

After the code was updated to meet the requirements of the assignment, API testing was carried out. It was discovered that all methods (GET, POST) were working perfectly well. 
At the same time, the error responses based on the type of input provided or lack thereof was also tested. All the tests passed successfully and produced desired outputs.

- Response logs and screenshots.

1. Home page

![](https://github.com/persianflower/Deep-Learning/blob/main/LNT_Task_5/outputs/flask_get.png)
   
2. Prediction 1

![](https://github.com/persianflower/Deep-Learning/blob/main/LNT_Task_5/outputs/flask_post_predict1.png)
  
3. Prediction 2

![](https://github.com/persianflower/Deep-Learning/blob/main/LNT_Task_5/outputs/flask_post_predict2.png)

4. Error handling

![](https://github.com/persianflower/Deep-Learning/blob/main/LNT_Task_5/outputs/flask_post_exception.png)

### Results

In this assignment only two actual predictions were carried out. As the aim of this project was to perform API testing and not to check whether the predictions were working correctly or not. The predictions were done solely for the testing of API working. After thorough trial and testing, the current workflow works for all cases. As discussed in previous task, the model accuracy is not optimal and could be improved for better results.


