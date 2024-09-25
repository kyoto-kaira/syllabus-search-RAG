FROM python:3.11-slim

COPY requirements.txt .

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    git \
    curl \
    && pip install --no-cache-dir -r requirements.txt \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /root/workspace
ENV PYTHONPATH=/root/workspace
