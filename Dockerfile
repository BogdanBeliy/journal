FROM python:3.8


ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /journal
RUN apt-get update && apt update

COPY req.txt /journal
RUN pip install --default-timeout=100 -r req.txt





