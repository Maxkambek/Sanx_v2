FROM python:3

ENV PYTHONUNBUFFERED 1
RUN mkdir /sanx_api
WORKDIR /sanx_api
COPY . /sanx_api/
RUN pip install -r requirements.txt


