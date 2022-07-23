FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /django-forum
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY ./src/ /django-forum/



