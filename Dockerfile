# DDOS INFINITY X — https://github.com/adilf/DDOS-INFINITY-X
FROM python:3.12-slim

LABEL maintainer="adil fayyaz"
LABEL org.opencontainers.image.source="https://github.com/adilf/DDOS-INFINITY-X"
LABEL org.opencontainers.image.title="DDOS INFINITY X"

WORKDIR /app

RUN apt-get update && apt-get install -y git && apt-get clean

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT ["python", "start.py"]
