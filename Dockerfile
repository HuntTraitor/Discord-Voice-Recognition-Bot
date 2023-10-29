FROM nikolaik/python-nodejs:latest
RUN apt-get -y update

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY package*.json ./
RUN npm install
RUN npm rebuild
COPY . .
RUN python -m pip install -r requirements.txt
