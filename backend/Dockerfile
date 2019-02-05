FROM python:3.7
MAINTAINER Richard Olsson <r@richardolsson.se>

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update
RUN apt-get install -q -y --force-yes --fix-missing python3-dev python3-pip
RUN apt-get install -q -y --force-yes libpq-dev
RUN apt-get install -q -y --force-yes git
RUN apt-get clean && rm -rf /var/lib/opt/lists/* /tmp/* /var/tmp/*

COPY requirements.txt /var/app/requirements.txt
WORKDIR /var/app

RUN pip3 install -r requirements.txt
COPY . /var/app

CMD ["python3", "-u", "manage.py", "runserver", "0.0.0.0:8000"]
