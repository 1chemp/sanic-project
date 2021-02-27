FROM ubuntu:18.04

COPY .  .

ENV NAME poroject

ENV LC_ALL=C.UTF-8

ENV LANG=C.UTF-8

RUN apt-get update && \
 apt-get -y install python3.8 && \
 apt-get -y install python3-pip && \
 pip3 install --upgrade pip && \
 pip3 --version && \
 apt-get -y install fail2ban && \
 pip install psycopg2-binary && \
 pip install ssh-import-id && \
 pip3 install ufw-config && \
 pip install uWSGI && \
 pip3 install Sanic-Cors && \
 pip3 install -r requirements.txt 

