from Crypto.Util.number import getPrime, bytes_to_long, long_to_bytes

with open("flag.txt", "rb") as f:
	flag = f.read()

p = getPrime(96)
q = getPrime(96)
e = 65537
n = p * q

m = bytes_to_long(flag)
c = pow(m, e, n)

print(f"n = {n}\ne = {e}\nc = {c}")