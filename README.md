# Angular-Flask-Docker-Skeleton
Simple Angular-Flask seed project with Docker.

This is the simple Angular-Flask web application skeleton. It is built with following components:
* Angular (4.2) - Frontend framework.
* Flask - Micro web framework (Python-3.6.2) for the backend.
* nginx - web server (It's also used for reverse proxy). External user hits the nginx which distributes the request between Frontend and Backend using url.
* uwsgi - It's a WSGI server that help running web application written in Python. It comes with direct support for popular NGINX web server.
* Docker - Usage of Docker Compose to build and host the application.
## Project Components (Directory Structure)
### client
This directory holds the Angular(4.2) code.
### nginx
This directory holds the nginx config file and Dockerfile for running the nginx container. This container serves the Angular code and also passes request to backend.
### server
This directory contains the server side code. It hosts the simple *Flask* app and *uswgi* file. It also has Dockerfile for running the flask container. This container hosts the backend code.
### docker-compose.yml
This file is used by the Docker to create the containers and run your app.

## Architecture
For this seed project, I am using 2 Docker containers:
* NGINX - Web Server
* FLASK - Flask web application with *uwsgi* server.

The two components are all created from Docker images that expand on the respective official images from Docker Hub. Each of these images are built using separate Dockerfiles. Docker Compose is then used to create all two containers and connect them correctly into a unified application.
### Working
The request from an external user hits the *nginx* web server on port 80. Depending on the __URL__,the request is served using Angular code or it is sent to Flask web application. In this app, all request URL starting with */api* is sent to Flask web service. The Flask docker container is also running and it exposes port 5000. These setting are defined in *nginx.conf* file. In this way, nginx is aware of both Frontend and Backend services.
### Basic Architecture Diagram
![alt text](https://github.com/mrsan22/Angular-Flask-Docker-Skeleton/blob/master/architecture.png)
## Usage
__NOTE__: Make sure you have Docker, node, npm and angular-cli installed.
* Clone this repository
* Navigate to client directory and execute `ng build --prod` to create production build for Angular.
* Then navigate back and execute following commands:
  * `docker-compose build`
  * `docker-compose up`
 * Open Browser and type following URL:
  * `localhost` - It should display the default Angular app
  * `localhost/api` - It should display welcome message from Flask.

This seed project is good for starting up with any Angular-Flask-Docker project, so check it out and feel free to fork, update, plug in your project etc. Let me know if you find any issues.

