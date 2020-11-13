#!/usr/bin/env python3

#
#
# hash-searcher.py md5|sha1|sha256|sha512 <RE>
#
#
# MineField
# OVH & Kimsufi Database

import hashlib,sys,re,random

def rand():
	rand = 'ClemleBOSS69'
	rand += str(random.randint(0,999999999999999999999999))
	return rand

try:
	if sys.argv[1] == 'md5':
		print("[+] Caculating MD5 hash with regex value as", sys.argv[2])
		while True:
			plain = rand()
			hashed = hashlib.md5(plain.encode()).hexdigest()
			if re.search(sys.argv[2], hashed):
				print("[*] Found hash: ",hashed, "with value", plain)

	if sys.argv[1] == 'sha1':
		print("[+] Caculating SHA1 hash with regex value as", sys.argv[2])
		while True:
			hashed = hashlib.sha1(rand().encode()).hexdigest()
			if re.search(sys.argv[2], hashed):
				print("[*] Found hash: ",hashed, "with value", rand())

	if sys.argv[1] == 'sha256':
		print("[+] Caculating SHA256 hash with regex value as", sys.argv[2])
		while True:
			hashed = hashlib.sha256(rand().encode()).hexdigest()
			if re.search(sys.argv[2], hashed):
				print("[*] Found hash: ",hashed, "with value", rand())

	if sys.argv[1] == 'sha512':
		print("[+] Caculating SHA512 hash with regex value as", sys.argv[2])
		while True:
			hashed = hashlib.sha512(rand().encode()).hexdigest()
			if re.search(sys.argv[2], hashed):
				print("[*] Found hash: ",hashed, "with value", rand())

except KeyboardInterrupt:
	print("[-] Interrupted!")

except:
	print("hash-searcher.py md5|sha1|sha256|sha512 <RE>")
