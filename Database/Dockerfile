# Stage 1: Build stage
# Stage 1: Build stage
FROM mariadb:latest as builder

# Set the root password for initialization
ENV MYSQL_ROOT_PASSWORD=root

# Copy the SQL script for initialization
COPY dbsetup.sql /docker-entrypoint-initdb.d/

# Initialize the database without starting the MySQL daemon
RUN mysqld --datadir=/initialized-db --aria-log-dir-path=/initialized-db --initialize-insecure

# Stage 2: Final stage
FROM mariadb:latest

# Copy the initialized database from the build stage
COPY --from=builder /initialized-db /var/lib/mysql

# Start the MySQL daemon in the final image
CMD ["mysqld"]
