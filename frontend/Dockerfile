FROM node:20

WORKDIR /app

COPY . .

RUN npm install -g @angular/cli@16
RUN npm install

CMD ["ng", "serve", "--host", "0.0.0.0"]
