import requests

payload = 'i /etc/natas_webpass/natas11'
username = 'natas11'
password = 'U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK'
url = "http://{}.natas.labs.overthewire.org/".format(username)
source = "http://{}.natas.labs.overthewire.org/index-source.html".format(username)

cookie = {'data': 'ClVLIh4ASCsCBE8lAxMacFMOXTlTWxooFhRXJh4FGnBTVF4sFxFeLFMK'}
session = requests.Session()

r = session.get(url, cookies=cookie, auth=(username, password))

text = r.text.split("\n")
res = "".join([i for i in text if 'natas12' in i]).split(" ")
output = res[3] + " : " + res[5][0:-4]
print(output)
