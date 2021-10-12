FROM python:3.9


ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app/journal
RUN mkdir /app/journal/static/
COPY req.txt .
RUN pip install --upgrade pip
RUN pip install -r req.txt
COPY . .




