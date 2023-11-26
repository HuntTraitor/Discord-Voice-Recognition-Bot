FROM python:3.10-slim
WORKDIR /app

COPY requirements.txt ./
RUN apt-get update && apt-get install git -y
RUN pip install -r requirements.txt
COPY --chown=myuser:myuser . .