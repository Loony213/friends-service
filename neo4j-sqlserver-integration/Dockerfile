FROM node:16

WORKDIR /app


COPY package.json package-lock.json ./


RUN npm install


COPY . .


EXPOSE 8002


CMD ["node", "index.js"]
