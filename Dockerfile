FROM ubuntu:14.04
FROM python:3.6

RUN apt-get update
COPY . .
RUN apt-get update
RUN apt-get -y install python-pip
RUN apt-get -y install git 
RUN pip install numpy
RUN git clone https://github.com/diloua/watershred_cicd
RUN cd watershred_cicd 
RUN python watershred.py f1_dinv.txt 2
