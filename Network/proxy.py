#Mine

import time
import sys, urllib
from thread import *
import socket


def start():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(('', 8080))
        s.listen(max_co)
        print ("[*] Init socket [8080] \n")
        print ("[*] Done")
    except Exception, e:
        print ("[*] Unable to init socket")
        print (e)
        sys.exit(2)

    while 1:
        try:
            conn, addr = s.accept()
            data = conn.recv(buffer_size)
            start_new_thread(conn_string, (conn,data, addr))
            print data # print url sent
        except KeyboardInterrupt:
            s.close()
            print ("[*] Closing socket")
            sys.exit(1)
    s.close()

def conn_string(conn, data, addr):
    try:
        first_line = data.split('\n')[0]
        url = first_line.split('')[1]
        http_pos = url.find("://")
        if (http_pos ==- 1):
            temp = url
        else:
            temp = url[(http_pos+3)]
        print url
        port_pos = temp.find(":")

        webserver_pos = temp.find("/")
        if (webserver_pos ==-1):
            webserver_pos = len(temp)
        webserver_pos=""
        port = -1
        if  (port_pos==-1 or webserver_pos < port_pos):
            port = 80
            webserver = temp[:webserver_pos]
        else:
            port = int((temp[(port_pos+1):])[:webserver_pos-port_pos-1])
            webserver = temp[:port_pos]

        proxy_server(webserver, port, conn, addr, data)

    except Exception, e:
        print e
        pass

def proxy_server(webserver, port, conn, data, addr):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((webserver, port))
        s.send(data)
        print data

        while 1:
            reply = s.recv(buffer_size)

            if (len(reply) > 0):
                conn.send(reply)
                dar = float(len(reply))
                dar = float(dar / 1024)
                dar = "%.3s" % (str(dar))
                dar = "%s KB" % (dar)
                'Print a custom message for request complete'
                print "[*] Request done: %s  => %s <=" %(str(addr[0]),str(dar))
            else:
                break
        s.close()
        conn.close()
    except socket.error, (value, message):
        s.close()
        conn.close()
        sys.exit(1)


max_co = 5 # simultaner Connection in queue
buffer_size = 1024 #max socket buffersize

# try :
#     listening_port = int(input("[*] Enter listening_port : "))
# except KeyboardInterrupt:
#     print ("\n[*]Exiting")
#     sys.exit


start()
