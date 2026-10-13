# Task 10: Containerizing Flask Deep Learning API

### Objective

To package a Flask-based deep learning API into a Docker container for deployment.

### Deliverables

- Dockerfile.

[Docker file](https://github.com/persianflower/Deep-Learning/blob/main/LNT_Task_10/Dockerfile)
  
- Docker Image.

The various statistics of the docker image can be viewed via the output folder:

[Image](https://github.com/persianflower/Deep-Learning/tree/main/LNT_Task_10/outputs/docker%20image%20ss)

- Deployment report.

The flask API application was deployed via the Dockerfile, which specified the base image it should be built upon. Here we chose a slim model of python 3.11 so as to save on space. Similarly the commands were seperated, with first copying the requirements file, running the file and only then copying the rest of the files. This ensures that in case of 
additional requirements being added later on the whole application need not be re-deployed, instead we can simply just copy the requirement files again. In order to check whether the api functionaility is running correctly, we made use of the api.py file. The outputs of the same have been made available to be viewed: [Output](https://github.com/persianflower/Deep-Learning/tree/main/LNT_Task_10/outputs)
