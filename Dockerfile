FROM python
WORKDIR /dir1/backend
COPY . /dir1/backend
CMD ["python","div.py"] 
