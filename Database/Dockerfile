# Stage 1: Build stage
FROM mariadb:latest as builder

# Modify the entrypoint script to only initialize the database, not run the MySQL daemon
RUN ["sed", "-i", "s/exec \"$@\"/echo \"not running $@\"/", "/usr/local/bin/docker-entrypoint.sh"]

# Set the root password for initialization
ENV MYSQL_ROOT_PASSWORD=root

# Copy the SQL script for initialization
COPY dbsetup.sql /docker-entrypoint-initdb.d/

# Set permissions for the initialization script
RUN chown -R mysql:mysql /docker-entrypoint-initdb.d/ &&\
  chmod -R 777 docker-entrypoint-initdb.d

# Initialize the database without starting the MySQL daemon
RUN ["/usr/local/bin/docker-entrypoint.sh", "mysqld", "--datadir", "/initialized-db", "--aria-log-dir-path", "/initialized-db"]

# Stage 2: Final stage
FROM mariadb:latest

# Copy the initialized database from the build stage
COPY --from=builder /initialized-db /var/lib/mysql

# Set the PATH to include the MySQL binaries directory
ENV PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/lib/mysql"

# Start the MySQL daemon in the final image
CMD ["mysqld"]
