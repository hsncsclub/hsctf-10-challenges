FROM tiangolo/uwsgi-nginx-flask:python3.10

RUN apt-get update && apt-get -y upgrade

RUN pip install wheel && pip install Flask==2.2.3

COPY ./app /app

RUN groupadd -r ctf && useradd -M -r -g ctf ctf

ENV LISTEN_PORT=80
EXPOSE 80
VOLUME /etc/nginx /tmp /var/ /run

