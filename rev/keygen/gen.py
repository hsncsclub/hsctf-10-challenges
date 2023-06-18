#!/usr/bin/env python3

with open("flag.txt", "rb") as f:
	flag = f.read()

print(bytes(c ^ 10 for c in flag))
