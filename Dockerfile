# Dockerfile
FROM python:3.11-slim

WORKDIR /app

# python dependencies
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# google cloud sdk
RUN apt-get update && apt-get install -y \
    curl \
    gnupg && \
    echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] http://packages.cloud.google.com/apt cloud-sdk main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list && \
    curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key --keyring /usr/share/keyrings/cloud.google.gpg add - && \
    apt-get update && apt-get install -y google-cloud-sdk

COPY . /app

ENV GOOGLE_APPLICATION_CREDENTIALS="/app/credentials.json"

CMD ["python", "main.py"]
