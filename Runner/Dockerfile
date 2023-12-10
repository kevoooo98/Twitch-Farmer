FROM ubuntu:latest

COPY Scripts/ /py-scripts/

ARG DEBIAN_FRONTEND=noninteractive

#install required apps
RUN apt update && \
  apt install software-properties-common python3.9 python3-pip -y
#install pip requirements
RUN pip install selenium &&\
  pip install pyotp &&\
  pip install pymysql
