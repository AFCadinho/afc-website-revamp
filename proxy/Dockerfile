FROM node:20-alpine AS build
WORKDIR /app

COPY frontend/web/package.json ./
COPY frontend/web/package-lock.json* ./
RUN npm install

COPY frontend/web/ ./
RUN npm run build

FROM nginx:stable-alpine
COPY proxy/nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=build /app/dist /usr/share/nginx/html