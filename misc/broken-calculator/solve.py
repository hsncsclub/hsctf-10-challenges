from pwn import *

r = remote('broken-calculator.hsctf.com', 1337)

for i in range(9):
	print(r.recvline())

k = 39
b = int(r.recvline()[-k - 1:])
m = 10 ** k
inv = pow(b, -1, m)

for i in range(1):
	print(r.recvline())

r.sendline("* " + str(inv))
r.sendline("--")
r.sendline("/ " + str(m))

for i in range(4):
	print(r.recvline())

a = int(r.recvline()[-k -1:])
c = (b * inv - 1) // m
a = ((a - c) * b % m)
print(a*m + b)
