FROM mariadb:latest

COPY Backend/Setup/dbsetup.sql /docker-entrypoint-initdb.d/
