FROM ubuntu:latest

COPY Scripts/ /py-scripts/

ARG DEBIAN_FRONTEND=noninteractive

RUN apt update && \
  apt install software-properties-common python3.8 python3-pip curl unzip wget xvfb libxi6 libgconf-2-4 -y &&\
  curl -LO https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb &&\
  apt-get install -y ./google-chrome-stable_current_amd64.deb &&\
  rm google-chrome-stable_current_amd64.deb &&\
  curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add &&\
  wget https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip &&\
  unzip chromedriver_linux64.zip &&\
  pip install selenium &&\
  mv chromedriver /usr/bin/chromedriver &&\
  chown root:root /usr/bin/chromedriver &&\
  chmod +x /usr/bin/chromedriver &&\
  python3 /pyscripts/main.py
