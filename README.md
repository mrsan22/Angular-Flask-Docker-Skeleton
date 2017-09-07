# Angular-Flask-Docker-Skeleton
Simple Angular-Flask seed project with Docker.

This is the simple Angular-Flask web application skeleton. It is built with following components:
* Angular (4.2) - Frontend framework.
* Flask - Micro web framework (Python) for the backend.
* nginx - web server (It's also used for reverse proxy). External user hits the nginx which distributes the request between Frontend and Backend using url.
* uwsgi - It's a WSGI server that help running web application written in Python. It comes with direct support for popular NGINX web server.
* Docker - Usage of docker-compose to build and host the application.
## Project Components
### client
This directory holds the Angular(4.2) code.
### nginx
This directory holds the nginx config file and Dockerfile for running the nginx container. This container serves the Angular code and also passes request to backend.
### server
This directory contains the server side code. It hosts the simple *Flask* app and *uswgi* file. It also has Dockerfile for running the flask container. This container hosts the backend code.
### docker-compose.yml
This file is used by the Docker to create the containers and run your app.
