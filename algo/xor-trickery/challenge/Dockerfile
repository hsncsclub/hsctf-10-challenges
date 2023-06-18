FROM python:slim AS app

FROM pwn.red/jail

COPY --from=app / /srv
COPY grader.py /srv/app/run
ENV JAIL_PORT=1337 JAIL_MEM=40M JAIL_ENV_PATH=/usr/local/bin JAIL_POW=15000
