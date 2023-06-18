#!/usr/bin/env python3
from pwn import *
import subprocess

#p = process("./grader")
p = remote("producing-3s.hsctf.com", 1337)
"""p.sendafter(
	b"solution: ",
	subprocess.run(p.recvline().decode().split(": ")[1], shell=True, stdout=subprocess.PIPE).stdout
)"""
i = p.recvuntil(b"Output:")
out = subprocess.run(["./solve"], input=i, check=True, stdout=subprocess.PIPE).stdout
p.send(out)
print(p.recvall().decode().strip())