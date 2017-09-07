FROM python:3.6.2

MAINTAINER Sanjiv Kumar "mr.san.kumar@gmail.com"

ENV PYTHONUNBUFFERED 1

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

ADD requirements.txt /usr/src/app/

RUN pip install --no-cache-dir -r requirements.txt

ADD main /usr/src/app

ADD ./main/uwsgi.ini /etc/uwsgi.ini

EXPOSE 5000

CMD uwsgi --ini /etc/uwsgi.ini