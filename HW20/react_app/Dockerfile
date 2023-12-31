FROM node AS build

WORKDIR /src

COPY package*.json .

RUN npm ci

COPY . .

RUN npm run build

FROM nginx

COPY --from=build /src/build /usr/share/nginx/html