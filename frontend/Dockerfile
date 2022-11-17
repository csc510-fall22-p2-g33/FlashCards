FROM node:16
WORKDIR /app

# Install requirements
COPY package.json package.json
RUN npm install --legacy-peer-deps

# Run application
COPY . .
EXPOSE 3000
ENTRYPOINT npm start