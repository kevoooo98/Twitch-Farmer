FROM php:8.0-apache

COPY ./ /var/www/html/

RUN docker-php-ext-install pdo pdo_mysql  &&\
  chmod -R 755 /var/www/html
