FROM tiangolo/uwsgi-nginx-flask:python3.10

RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y cron

COPY ./app/requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

COPY ./app /app
COPY ./flag.txt /app/flag.txt

RUN groupadd -r ctf && useradd -M -r -g ctf ctf && \
	mkdir -p /upload/ && chown root:ctf /upload && chmod 773 /upload/ && \
	chmod 744 /app/flag.txt && \
	echo "sub hard nproc 64" >> /etc/security/limits.conf && \
	echo "*/15 * * * * ctf rm -f /upload/*" >> /etc/crontab



ENV LISTEN_PORT=80
EXPOSE 80
VOLUME /etc/nginx /tmp /var/ /run /upload
