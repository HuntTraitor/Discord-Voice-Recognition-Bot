FROM tensorflow/tensorflow:latest-gpu
WORKDIR /app

COPY requirements.txt ./
RUN apt-get update && apt-get install git -y
RUN apt-get install -y ffmpeg
RUN pip install -r requirements.txt --ignore-installed
COPY --chown=myuser:myuser . .