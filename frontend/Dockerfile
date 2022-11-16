FROM node:16
WORKDIR /app

COPY . .
RUN npm install --legacy-peer-deps

EXPOSE 3000

ENTRYPOINT npm start