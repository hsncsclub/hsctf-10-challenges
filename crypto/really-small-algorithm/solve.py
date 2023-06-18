import requests
from utils.crypto.rsa import decrypt_to_str

from Crypto.Util.number import long_to_bytes

# if factordb is down, use https://www.alpertron.com.ar/ECM.HTM
API_URL = "http://www.factordb.com/api"

def factors(n: int) -> list[int]:
	resp = requests.get(API_URL, params={"query": str(n)}).json()
	return [int(factor[0]) for factor in resp["factors"] for _ in range(factor[1])]

n = 0
e = 0
c = 0

with open("out.txt") as f:
	exec(f.read())

p, q = factors(n)
totient = (p - 1) * (q - 1)
d = pow(e, -1, totient)
print(long_to_bytes(pow(c, d, n)).decode())
