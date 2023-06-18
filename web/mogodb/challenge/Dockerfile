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

ENV FLAG=flag{easier_than_picture_lab_at_least} \
	FLASK_SECRET=f9f7be0dc95b26e2e32e3073ceda643c1b4b682939ee9dc70d40384acb994b1b \
	ADMIN_SECRET=925eb585f6478e66f37d58457eda0d780255c0c2fc9bc656bcab6b5b1d993331 \
	LISTEN_PORT=80
EXPOSE 80
VOLUME /etc/nginx /tmp /var/ /run /data
