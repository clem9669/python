#!/usr/bin/env python3

import requests
import json
import re

#Wireshark: export to json
f = open(file='export-json.json',mode='r')
e = open(file='output.txt', mode='w+')
parsed_json = json.load(f)

for i in range(34):
    e.write(str(i) +":" + json.dumps(parsed_json[i]['_source']['layers']['icmp']['data']['data.data']).replace(":",""))
    e.write("\n")


# remove none 256 length: line 0 3

#get all unique bytes among all other packets
#unique_after_correction = """\x8ba\\cZ\x8e^\\`\x8c`\x8b[a`^\x8b\x90`\x90\x8ea\x90\x8c\x8b_\x8e\x8c\\[^\x8f"""
unique = """dgY\xa64\xa5d\x87\x85WOj\x85OdP\x88XiU\x88PiYVSPj\xa6\x88RdX\x85ddR\x87hh\xa5UXYdfOPY\xa8jd\xa7O\x85UfOTYWYTUf\xa8VTY4fSTh\x87US\x85\x87X\xa8OgVOUO\x88\xa8f\x85ThhiWY\xa6TSi\x88\x88OdgVUXdj\xa7TTSUYR\x87Sd\x88gYfgX\rS\xa6\x85\xa8\xa6Sf4gXgdd\xa5V\xa5VY\x88\x87TUR\x85O\x85TU\xa8R\xa6XiVfXd\xa6gVV\xa7d\xa7jf\xa5UOPPTfS\xa8\x88X\xa5W\xa5S\x85jS\xa6\xa8gjdYdT4\xa7\xa6\xa7\x88RgXT\x85Y\xa7ji\x85OUUVdRSjV\xa8Ti\x87V\xa7\x88h\x87PY\xa7S\x88d\xa7OVddT\xa7\x85jWigSj\xa8\xa8\r\x8ba\\cZ\x8e^\\`\x8c`\x8b[a`^\x8b\x90`\x90\x8ea\x90\x8c\x8b_\x8e\x8c\\[^\x8f"""

# cesar code on ascii table
all = []
for i in range(256):
  all.append(repr(''.join([chr((ord(c)+i)%256) for c in unique])))


#identify possible result & md5 Hash length= 32
for i in range(0,255):
    if len(re.sub(r'[^a-z0-9]', "", all[i])) < 40:
        print(str(i) + ":" + re.sub(r'[^a-z0-9]', "", all[i]))


#number 214 seems to be a correct possible md5 hash
