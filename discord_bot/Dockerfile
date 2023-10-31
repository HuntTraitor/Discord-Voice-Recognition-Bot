FROM node:20
WORKDIR /app

RUN apt-get update
COPY package*.json ./
RUN npm install

COPY --chown=myuser:myuser . .