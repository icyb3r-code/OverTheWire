import requests
from bs4 import BeautifulSoup


username='natas22'
password='chG9fbe1Tq2eWVMgjYYD1MsfIvN461kJ'
url ="http://{}.natas.labs.overthewire.org/".format(username) #?debug=True

param = {'revelio':'anythinghere'}

s = requests.Session()

r = s.get(url,params=param,auth=(username,password),allow_redirects=False)
sp = BeautifulSoup(r.text,"lxml")
pre = sp.find_all('pre')

print(pre[0].text)