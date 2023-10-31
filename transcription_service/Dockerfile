FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt ./
RUN apt-get update && apt-get install git -y
RUN pip install -r requirements.txt
RUN pip install "git+https://github.com/openai/whisper.git" 
RUN apt-get install -y ffmpeg
COPY --chown=myuser:myuser . .
