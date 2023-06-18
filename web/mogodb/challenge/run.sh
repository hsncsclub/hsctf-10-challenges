#!/bin/sh
su mongodb -s /bin/sh -c 'mongod > /var/log/mongod.log' &
sleep 1
mongosh database --eval "db.users.insertOne({'user':'admin','password':'$ADMIN_SECRET','admin':true})"
exec /start.sh