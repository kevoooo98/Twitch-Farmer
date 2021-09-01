FROM php:8.0-apache

COPY Frontend/ /var/www/html/

RUN docker-php-ext-install pdo && docker-php-ext-enable pdo
