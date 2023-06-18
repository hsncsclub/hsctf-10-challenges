#!/bin/sh
mariadbd -umysql &
sleep 3
mariadb <<HERE
CREATE DATABASE ctf;
USE ctf;
CREATE USER 'ctf'@localhost IDENTIFIED BY '$DB_PASSWORD';
CREATE TABLE users (
	id INT NOT NULL AUTO_INCREMENT,
	data JSON,
	PRIMARY KEY(id)
);
GRANT ALL PRIVILEGES ON *.* TO 'ctf'@localhost;
INSERT INTO users (data) VALUES ('{"user": "admin", "password": "$ADMIN_PASSWORD", "admin": true}');
FLUSH PRIVILEGES;
HERE
exec /start.sh