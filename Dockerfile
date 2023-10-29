FROM node:18
WORKDIR /app
COPY packages/package*.json ./
RUN npm install
COPY . .