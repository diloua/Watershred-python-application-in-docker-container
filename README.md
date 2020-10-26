# Watershred-python-application-in-docker-container

## Description

The python application applies a watershred transformation to a greyscale image.
This application is ran inside a Docker container. 

## How to run

#Run inside the container :
docker build . 
Builds the dockerfile and creates a container that runs the application. 

#Run directly

python watershred file.txt watershredlevel 

file.txt : csv representation of grayscale image
watershredlevel: int representing the level of the watershred

Example : python watershred f1_dinv.txt 2


