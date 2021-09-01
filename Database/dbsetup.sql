CREATE USER 'dbuser'@'%' IDENTIFIED BY 'geheim1';
GRANT ALL PRIVILEGES ON *.* to 'dbuser'@'%' WITH GRANT OPTION;

CREATE DATABASE twitchfarm;

USE twitchfarm;

CREATE TABLE streams (
  ID_Stream int primary key auto_increment,
  url varchar(255),
  watchtime int,
  fav bit
);
