FROM phusion/baseimage:0.11

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y nginx
RUN apt-get install -y python-pip
RUN apt-get install -y letsencrypt

RUN pip install envtpl

RUN echo 'daemon off;' >> /etc/nginx/nginx.conf

RUN mkdir /etc/service/nginx
ADD run.sh /etc/service/nginx/run

ADD insecure.conf /etc/nginx/sites-templates/

ADD manual.conf /etc/nginx/sites-templates/
ADD www.conf /etc/nginx/sites-templates/
