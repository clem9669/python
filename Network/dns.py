import sys,socket


def getIP(url):
    dns_query=socket.getaddrinfo(url,None)
    # print (dns_query) // all stuff (tcp-udp)

    i = 0 # list (tcp = socket.SOCK_STREAM - udp = socket.SOCK_DGRAM)
    for items in dns_query:
        print (i,":",items[4])
        i+=1

def reverseDns(ip):
    dns_query = socket.gethostbyaddr(ip)
    print(dns_query)



#getIP("google.fr")
reverseDns("8.8.8.8")

print("\n")
print("press Enter to quit")
input() # wait until the user press enter
print("[*] Done")
exit(0)
