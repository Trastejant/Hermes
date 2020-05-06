FROM python:latest

RUN apt update 
RUN apt install python-mysqldb

ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD python entrypoint.py