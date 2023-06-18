FROM tiangolo/uwsgi-nginx-flask:python3.10

RUN apt-get update && apt-get -y upgrade 
RUN curl -o /etc/apt/trusted.gpg.d/mariadb_release_signing_key.asc 'https://mariadb.org/mariadb_release_signing_key.asc' && \
	echo 'deb https://ftp.osuosl.org/pub/mariadb/repo/10.11/debian bullseye main' >>/etc/apt/sources.list && \ 
	apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 0xF1656F24C74CD1D8 && \ 
	apt-get update && apt-get install -y mariadb-server mariadb-client libmariadb3 

RUN groupadd -r ctf && useradd -M ctf -g ctf

RUN pip install --upgrade pip
COPY requirements.txt /
RUN pip install -r /requirements.txt

COPY ./app /app

COPY ./run.sh /run.sh
RUN chmod 700 /run.sh
CMD ["/run.sh"]

RUN mkdir -p /run/mysqld && chown -R mysql:mysql /run/mysqld

ENV FLAG=flag{imagine_not_fixing_a_bug_mysql_fixed_five_years_ago} \
	FLASK_SECRET=9d3c41291c65f0bc5233d4483297fb09fc384b2a46caeb22707ad6e38ddbbae2 \
	DB_PASSWORD=e600ad7e372105e8fa0bf7ab7f410e3cf06e130b6dfe2d67a66bdc87adc6c482 \
	ADMIN_PASSWORd=31cd859e5b1cced74139ba81fdb522182f69d11490fc4d2e5dabced7a76152b2 \
	LISTEN_PORT=80
EXPOSE 80
VOLUME /etc/nginx /tmp /var/ /run
