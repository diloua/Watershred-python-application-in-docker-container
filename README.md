# Watershred-python-application-in-docker-container

## Description
"
The python application applies an image segmentation operation called "watershred transformation" to a greyscale image. The aim of this technique is to segment the image, typically when two regions-of-interest are close to each other.

We inject CI/CD tools to this application, it is built inside a docker container and the docker image is push in a repository in dockerhub. 

## Running the application inside with docker 

### Run inside the container :

`docker build -t image_name .`  

Builds the dockerfile and creates a container that runs the application. 

`docker push user_id/image_name:tag_name`  

Pushes the docker in the dockerhub repository 

Our docker image is pushed in 

https://hub.docker.com/repository/docker/oualidelbouanani/watershred_v1


### Run directly

`python watershred file.txt watershredlevel`

file.txt : csv representation of grayscale image (ie: f1_dinv.txt)
watershredlevel: int representing the level of the watershred(ie : 2 or 4 or 8 )

Example : python watershred f1_dinv.txt 2


