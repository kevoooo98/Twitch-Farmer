FROM fauria/lamp

COPY Frontend/ /var/www/html/
COPY Backend/Setup/twitchfarm/ /var/lib/mysql/twitchfarm/

RUN  service mysql start &&\
  mysql -e"CREATE USER 'dbuser'@'localhost' IDENTIFIED BY 'geheim1';" &&\
  mysql -e"GRANT ALL PRIVILEGES ON *.* TO 'dbuser'@'localhost' WITH GRANT OPTION;"
