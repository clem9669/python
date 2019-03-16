#!/usr/bin/env python3
import re
import base64

mot="bonjour"
secret="Ym9uc29pcg=="
# encoding utf8 ascii hex
print(ord('A')) # ascii to decimal
print(bin(41)) #decimal to binary
print(hex(65)) #decimal to hex

# utf8 to hex
string=mot.encode(encoding='utf_8') #encoding mandatory
print(string.hex())

# base encode decode
# binary 0b or 0B to base10
print("For 1010, int is:", int('1010', 2))
print("For 0b1010, int is:", int('0b1010', 2))

# octal 0o or 0O to base10
print("For 12, int is:", int('12', 8))
print("For 0o12, int is:", int('0o12', 8))

# hexadecimal to base10
print("For A, int is:", int('A', 16))
print("For 0xA, int is:", int('0xA', 16))

#base64 encode decode
base64.b64encode(string)
base64.b64decode(secret)

# manipulating regex:
sample = "t provides a gentler introduction 9099988 than the corresponding section in the Library Reference."

# Function 	Description
# findall 	Returns a list containing all matches
# search 	Returns a Match object if there is a match anywhere in the string
# split 	Returns a list where the string has been split at each match
# sub 	    Replaces one or many matches with a string

# Character 	Description 	Example
# []    	A set of characters 	"[a-m]"
# \ 	    Signals a special sequence "\d"
# . 	    Any character (except newline character) "he..o"
# ^ 	    Starts with            	"^hello"
# $ 	    Ends with 	            "world$"
# * 	    Zero or more occurrences  "aix*"
# + 	    One or more occurrences    "aix+"
# {} 	    Exactly the specified number of occurrences "al{2}"
# | 	    Either or              	"falls|stays"
# () 	    Capture and group

#only alphAnumeric
print(re.findall("[A-Za-z0-9]",sample))
print(re.sub("[0-9]","",sample))
print(re.sub("[^0-9]","",sample)) #9099988
