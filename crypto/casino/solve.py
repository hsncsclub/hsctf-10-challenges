import json

from Crypto.Util.strxor import strxor
from pwnlib.tubes.process import process
from pwnlib.tubes.remote import remote

#p = process("./test.sh")
p = remote("casino.hsctf.com", 1337)

# get some amount of money
p.sendlineafter(b"> ", b"2")
p.sendlineafter(b"> ", b"5")
p.recvuntil(b"now have ")
money = float(p.recvuntil(b" "))
p.sendlineafter(b"> ", b"2")

# get save token
p.sendlineafter(b"> ", b"4")
p.recvuntil(b": ")
nonce, ct = p.recvall().decode().split(".")
ct = bytes.fromhex(ct)

# CTR bit-flipping
pt = json.dumps({"money": money}).encode()
target = json.dumps({"money": float("nan")}).ljust(len(pt)).encode()  # or 1e10
new_ct = strxor(strxor(pt, target), ct)
new_token = f"{nonce}.{new_ct.hex()}".encode()

# use modified token
# p = process("./test.sh")
p = remote("casino.hsctf.com", 1337)
p.sendlineafter(b"> ", b"3")
p.sendlineafter(b"> ", new_token)
p.sendlineafter(b"> ", b"1")
print(p.recvline().decode(), end="")
