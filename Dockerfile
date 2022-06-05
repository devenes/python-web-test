FROM python:3.7-slim-buster as builder

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc

COPY requirements.txt ./

RUN pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt


# Build the app image from the wheel files 
FROM python:3.7-slim-buster

WORKDIR /app

COPY --from=builder /app/wheels /wheels
COPY --from=builder /app/requirements.txt ./

RUN pip install --no-cache /wheels/*
