FROM python:3.4
MAINTAINER Richard Olsson <r@richardolsson.se>

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update
RUN apt-get install -q -y --force-yes --fix-missing python3-dev python3-pip
RUN apt-get install -q -y --force-yes libpq-dev
RUN apt-get install -q -y --force-yes git

RUN pip3 install Django==2.0
RUN pip3 install psycopg2
RUN pip3 install django-cms
RUN pip3 install django-filer
RUN pip3 install djangocms-text-ckeditor
RUN pip3 install djangocms-link djangocms-picture djangocms-column

RUN apt-get clean && rm -rf /var/lib/opt/lists/* /tmp/* /var/tmp/*

WORKDIR /var/app
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
