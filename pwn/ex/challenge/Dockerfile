FROM ubuntu:20.04 as chroot

RUN apt update && apt install -y gcc libc6-dev
RUN /usr/sbin/useradd --no-create-home -u 1000 user

COPY flag.txt /
COPY chall.c gen.sh /home/user/
RUN cd /home/user && ./gen.sh && rm chall.c gen.sh

FROM gcr.io/kctf-docker/challenge@sha256:0f7d757bcda470c3bbc063606335b915e03795d72ba1d8fdb6f0f9ff3757364f

COPY --from=chroot / /chroot

COPY nsjail.cfg /home/user/

CMD kctf_setup && \
    kctf_drop_privs \
    socat \
      TCP-LISTEN:1337,reuseaddr,fork \
      EXEC:"nsjail --config /home/user/nsjail.cfg -- /home/user/ex"
