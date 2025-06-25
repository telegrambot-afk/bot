FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install -y libreoffice libreoffice-writer fonts-dejavu-core && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /app/media

WORKDIR /app/

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY himik_bot /app/

EXPOSE 8000