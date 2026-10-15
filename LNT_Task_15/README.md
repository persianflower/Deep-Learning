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
- Create a Streamlit frontend.
- Containerize using Docker.
- Deploy using Kubernetes.
- Optionally publish using Streamlit Cloud.
- Monitor application performance.

### Deliverables

- Complete project source code.
- Trained model.
- Docker and Kubernetes configuration files.
- Deployment URL (if cloud hosted).
- Final project report and presentation.
