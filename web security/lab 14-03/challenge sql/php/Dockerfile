FROM php:7.4-cli-alpine
RUN docker-php-ext-install mysqli pdo pdo_mysql
COPY ./index.php /usr/src/myapp/index.php
WORKDIR /usr/src/myapp
EXPOSE 5200
CMD ["php", "-S", "0.0.0.0:5200", "./index.php"]
