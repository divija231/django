# FROM python
# WORKDIR /dir1/backend
# COPY . /dir1/backend
# CMD ["python","div.py"] 

FROM httpd:latest

COPY div.html /usr/local/apache2/htdocs/

EXPOSE 80
