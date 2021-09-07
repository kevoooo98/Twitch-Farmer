FROM ubuntu:latest

COPY Scripts/ /py-scripts/

ARG DEBIAN_FRONTEND=noninteractive

#install required apps
RUN apt update && \
  apt install software-properties-common python3.8 python3-pip curl unzip wget xvfb libxi6 libgconf-2-4 libxss1 fonts-liberation libasound2 libatk-bridge2.0-0 libatk1.0-0  libatspi2.0-0 libcairo2 libcups2 libdrm2 libgbm1 libglib2.0-0 libgtk-3-0 libnspr4 libnss3 libpango-1.0-0 libxcomposite1 libxdamage1 libxfixes3 libxkbcommon0 libxrandr2 libxshmfence1 xdg-utils xvfb -y
# Add a user for running applications.
RUN useradd apps
RUN mkdir -p /home/apps && chown apps:apps /home/apps

#install chrome
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb &&\
  dpkg -i google-chrome-stable_current_amd64.deb
#Install Selenium
RUN wget https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip &&\
   unzip chromedriver_linux64.zip
#install pip requirements
RUN pip install selenium &&\
  pip install pyotp &&\
  pip install pymysql &&\
  pip install webdriver-manager &&\
  pip install pyvirtualdisplay
