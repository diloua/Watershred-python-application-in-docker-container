FROM ubuntu:14.04
FROM python:3.6

RUN apt-get update
WORKDIR usr/cv_projects/watershred 
COPY . .
RUN apt-get update
RUN apt-get -y install python-pip
RUN apt-get -y install git 
RUN pip install numpy
RUN ls
RUN python watershred.py f1_dinv.txt 2
