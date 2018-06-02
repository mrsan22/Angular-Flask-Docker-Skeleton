The Dockerfile for postgresql lives here. It has not been included due to sensitve information 
related to database.

### Sample Dockerfile
FROM postgres:9.6

MAINTAINER Sanjiv Kumar "<your_email>"

ENV POSTGRES_USER 'username'<br />
ENV POSTGRES_PASSWORD 'password'<br />
ENV POSTGRES_DB 'db_name'