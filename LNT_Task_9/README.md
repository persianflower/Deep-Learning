# Task 9: Docker Fundamentals and Container Lifecycle Management

### Objective

To understand Docker architecture and manage containerized deep learning applications.

### Deliverables

• Docker command logs.

[Commands]()

• Practical implementation report.

As per the task given, following concepts were studied and executed on docker:

1. Basic commands related to introduction to docker
2. Creation of container and its management
3. Creation of images
4. Container lifecycle operation
5. Networking operations

• Screenshots and observations.

1. Basic commands related to introduction to docker

![Basic commands screenshots]()

Here, we observed how to install docker as well as how to check whether it is correctly working on our system. Only basic checking of docker, its version and help commands were executed 
in this step.

2. Creation of container and its management

![Container screenshots]()

For all the commands henceforth, nginx a basic docker hub repository was used. We used it to understand various commands
as well as to execute operations. 

In this section, we learnt how to create a container, how to name it, how to run it in the background as well as how to view all the 
docker containers available in our system.

All these commands were carried out on the CLI instead of directly accessing via the docker desktop dashboard, which 
provides intuitive usecase.

3. Creation of images

![Images screenshots]()

Here, were learnt how to pull images to be used as well as how to customize the type of image to be pulled.
We also learnt how to delete an already existing image as well as the best practises associated with it.
How to create a new image was also learnt in this section.

4. Container lifecycle operation

![Lifecycle screenshots]()

The docker container follows a fixed lifecycle and the operations can only be carried out if they exist in the
valid form. Following operations are allowed:

- create -> run
- create -> delete
- run -> stop
- run -> pause
- stop -> delete

Some things become clear after viewing the legal moves, a container which is currently running cannot be removed.
That is we cannot delete an executing container. However, docker does allow us to bypass this rule via the `-f` flag.
However, it is best practise to instead stop a container before deleting it. 

5. Networking operations

![Networking screenshots]()

Docker allows a container to be connected to custom networks which was utilised in this section. We created our own network
on which then we ran our container.
