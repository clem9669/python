# -*-coding: utf-8 -*
import socket, sys

host = sys.argv[1]
port = sys.argv[2]
port = int(port)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socked created!")

try:
    ip = socket.gethostbyname(host)
except socket.gaierror:
    print("invalid host ")
    sys.exit(1)

print("IP Address of " + host + " is " + ip)

s.connect((ip, port))
print("Socket connected to " + host + " on ip " + ip)

message = b"GET / HTTP/1.1\r\n\r\n" # send as bytes
s.sendall(message)

data = s.recv(4096)
print(data)
s.close
