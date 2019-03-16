#export PYTHONIOENCODING=utf-8
import requests, sys, os
import json
from bs4 import BeautifulSoup

# Problems:
# auto detect type in server response content-type then parse + beautify
# handle invalid uri

def banner():
    print("  ___  _  _  ____  __")
    print("/ __)/ )( \(  _ \(  )")
    print("( (__ ) \/ ( )   // (_/\ ")
    print("\___)\____/(__\_)\____/")

def whole_url(url):
    headers = {'user-agent': 'Mozilla/4.0 (PSP (PlayStation Portable); 2.00)'}
    url2 = "https://" + url.replace('http://','').replace('https://','')
    req = requests.get(url2, headers=headers)
    return req

def result(url):
    print("\nThis is the result of the page: ", whole_url(url).url)
    print("\nThe time elapsed is: ", whole_url(url).elapsed)
    print("\nHeaders: ", whole_url(url).headers)
    #print("\nContent-json:" , whole_url(url).text)
    print("\nContent-html:" , BeautifulSoup(whole_url(url).text,features="html.parser").prettify()) #https://stackoverflow.com/questions/50045775/lxml-beautifulsoup-parser-warning

def main():
    banner()
    if len(sys.argv) == 1:
        while True:
            url = input("Enter a URL: (www.wikipedia.org) \n")
            result(url)
    elif len(sys.argv) == 2:
        url = sys.argv[1]
        result(url)
    else:
        print (" Too much args ")
        exit(0)
try:
    main()
except KeyboardInterrupt:
    os.system('clear')
    exit(0)
