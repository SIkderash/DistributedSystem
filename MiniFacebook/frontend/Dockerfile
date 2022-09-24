FROM node:alpine AS frontend
WORKDIR /app
COPY . .
RUN npm install
RUN npm install -g @angular/cli
CMD ["ng", "serve", "--host", "0.0.0.0:4000"]