FROM nginx:alpine

MAINTAINER Sanjiv Kumar "mr.san.kumar@gmail.com"

# Copy custom nginx config
COPY ./nginx/nginx.conf /etc/nginx/nginx.conf
COPY ./nginx/cert.pem /etc/nginx/cert.pem
COPY ./nginx/key.pem /etc/nginx/key.pem

EXPOSE 80 443

ENTRYPOINT ["nginx"]
CMD ["-g", "daemon off;"]