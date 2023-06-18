FROM python:3.9-slim AS app

FROM pwn.red/jail

COPY --from=app / /srv
COPY flag.txt /srv/app/flag.txt
COPY main.py /srv/app/run
ENV JAIL_PORT=1337 JAIL_MEM=20M JAIL_ENV_PATH=/usr/local/bin JAIL_TIME=120
