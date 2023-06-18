#!/bin/sh
su mongodb -s /bin/sh -c 'mongod > /var/log/mongod.log' &
sleep 1
mongosh database <<HERE
db.flags.insertOne({'challenge':'west-side-story', 'flag':'flag{fake_flag}', price: 5})
db.flags.insertOne({'challenge':'png-wizard-v3', 'flag':'flag{fake_flag}', price: 1000})
db.flags.insertOne({'challenge':'flag-shop', 'flag':'$FLAG', price: 10})
db.flags.insertOne({'challenge':'fancy-page-v2', 'flag':'flag{fake_flag}', price: 1})
db.flags.insertOne({'challenge':'fancy-page', 'flag':'flag{fake_flag}', price: 12})
HERE
exec /start.sh