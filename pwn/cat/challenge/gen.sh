#!/bin/sh
gcc -o chall chall.c -fno-stack-protector -no-pie -Wall -Wextra -m32
