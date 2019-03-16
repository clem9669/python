# coding: utf-8
import zipfile
import argparse

parser = argparse.ArgumentParser(description="Python bruteforce script on zipfile. \nUsage: python3 zip-bruteforce.py -f ./zip.zip -w ./wordlist.lst")
parser.add_argument("-f", "--filename", help="zip file path", type=str, required=True)
parser.add_argument("-w", "--wordlist", help="path to the wordlist", required=True)
args = parser.parse_args()

path_zip = args.filename
wordlist =  args.wordlist

password = None

zip_file = zipfile.ZipFile(path_zip)
with open(wordlist, 'r') as f:
	for line in f.readlines():
            password = line.strip('\n')
            try:
                zip_file.extractall('.',pwd=password)
                password = 'Password found: %s' % password
            except KeyboardInterrupt:
                exit(0)
            except:
                pass
print(password)
