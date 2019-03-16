# -*-coding: utf-8 -*
import socket,sys

# GOAL:
# connect
# read banner
# send USER
# read response
# close

host = "ftp.fr.debian.org/debian/"
port = 21

# def fini():
#     data = s.recv(4096)
#     print("data")
#     if data=="":
#         pass

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
data = s.recv(4096)
print("data")

s.send("USER demo \r\n")
data = s.recv(4096)
print("data")

s.send("PASS password \r\n")
data = s.recv(4096)
print("data")


s.send("HELP \r\n")
data = s.recv(4096)
print("data")

s.send("QUIT \r\n")
data = s.recv(4096)
print("data")
