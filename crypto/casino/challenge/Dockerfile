FROM python:slim AS app
RUN pip install wheel && pip install pycryptodome

FROM pwn.red/jail

COPY --from=app / /srv
COPY casino.py /srv/app/run
ENV JAIL_PORT=1337 JAIL_MEM=20M JAIL_ENV_PATH=/usr/local/bin
ENV JAIL_ENV_FLAG="flag{you're_ready_for_vegas_now}"
ENV JAIL_ENV_KEY=a89b9f3b6d5a0c805fe83f15a42a2f0d
