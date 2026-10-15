# Task 15: End-to-End Deep Learning Production Deployment Project

### Objective

To design, develop, containerize, orchestrate, and deploy a complete end-to-end deep learning
application following industry-standard MLOps practices.

### Approach

- Develop and train the deep learning model.

The CIFAR-10 dataset was used to train this model. Here we made three deep learning models namely: ANN, CNN as 
well as a deep CNN which is simply a CNN with more layers. Of these ANN performed the most poorly with a high
validation loss and the best performing model was the deep CNN. For the rest of the project the model trained
on deep CNN is used which was downloaded via pickle.

- Build a Flask API.

The backend was prepared with the help of Flask. Here we created API routes to be used by streamlit to predict
images. 

- Create a Streamlit frontend.

Our frontend was linked with flask via its api_url. To run the app we need to run both flask as well as streamlit
as the model is loaded in flask and input is taken from streamlit.

- Containerize using Docker.

After the app was created following commands were followed to container the app.

1. Create image of app

```code
docker build -t cifar-application .  
```

2. Tag the image

```code
docker tag cifar-application:latest ayeshafaquih/cifar-10-application:latest 
```

3. Push to docker hub

```code
docker push ayeshafaquih/cifar-10-application:latest
```

4. Run the container

```code
docker run -p 8501:8501 cifar-application 
```

- Deploy using Kubernetes.

1. Start the minikube via docker

```code
minikube start --driver=docker
```

2. View the dashboard

```code
minikube dashboard
```

3. View pods

```code
kubectl get pods
```

4. View services

```code
kubectl get svc
```

5. View ip address

```code
minikube ip
```

- Monitor application performance.

This was done via the minikube dashboard

### Deliverables

- Trained model.

[Trained model](https://github.com/persianflower/Deep-Learning/blob/main/LNT_Task_15/model_deep.pkl)

- Docker and Kubernetes configuration files.

[Dockerfile](https://github.com/persianflower/Deep-Learning/blob/main/LNT_Task_15/Dockerfile)

[Deployment](https://github.com/persianflower/Deep-Learning/blob/main/LNT_Task_15/deployment.yaml)

- Hosted site

[Site](https://cifar-10-project.streamlit.app/)

