FROM tiangolo/uwsgi-nginx-flask:python3.10

RUN apt-get update && apt-get -y upgrade 
RUN wget -O - https://www.mongodb.org/static/pgp/server-6.0.asc | apt-key add - && \
	echo "deb http://repo.mongodb.org/apt/debian bullseye/mongodb-org/6.0 main" > /etc/apt/sources.list.d/mongodb-org-6.0.list && \
	apt-get update && apt-get install -y mongodb-org

RUN groupadd -r ctf && useradd -M ctf -g ctf

RUN pip install --upgrade pip
COPY requirements.txt /
RUN pip install -r /requirements.txt

COPY ./app /app

COPY ./run.sh /run.sh
RUN chmod 700 /run.sh
CMD ["/run.sh"]

RUN mkdir -p /data/db /data/configdb && touch /var/log/mongod.log && \
	chown -R mongodb:root /data/db /data/configdb /var/log/mongod.log

ENV FLAG=flag{hsctf_gacha_game_when?} \
	FLASK_SECRET=4bfd6c22526f00b7b7260d35b721116cafb66e6cca10f8fc1598f52004f6461a \
	LISTEN_PORT=80
EXPOSE 80
VOLUME /etc/nginx /tmp /var/ /run /data
