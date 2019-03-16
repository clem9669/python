# -*-coding: utf-8 -*
import socket

host=socket.gethostbyname(socket.gethostname())
port=1236

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind((host,port))
s.listen(1)

client, addresses = s.accept()
print(addresses)
print("connection from: ", client.getpeername())
client.send("Hi bud:")
while 1:
    data=client.recv(1024)
    if data == "stop":
        break
    print("client > ", data)
    word = raw_input("server > ")
    client.send(word)
client.close()
s.close
