import socket
import sys
import base64
import hashlib
from _thread import *
host = ''
port = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host,port))
s.listen(5)

MAGIC_GUID = "258EAFA5-E914-47DA-95CA-C5AB0DC85B11".encode("utf-8")

handshake = '\
HTTP/1.1 101 Web Socket Protocol Handshake\r\n\
Upgrade: WebSocket\r\n\
Connection: Upgrade\r\n\
Sec-WebSocket-Accept: {}\r\n\
Server: Test\r\n\
Access-Control-Allow-Origin: http://localhost:5555/\r\n\
Access-Control-Allow-Credentials: true\r\n\r\n\
'.format(base64.b64encode(hashlib.sha1(MAGIC_GUID).digest()).decode('utf-8'))
print(handshake)
def threaded_client(conn):
    header = ''
    data = ''
    handshaken = False
    while handshaken == False:
        header += conn.recv(16).decode("utf-8")
        #rint(header)
        if header.find('\r\n\r\n') != -1:
            data = header.split('\r\n\r\n', 1)[0]
            conn.send(str.encode(handshake))
            handshaken = True
    print("hand equals shook")
    #print(header)
    tmp = conn.recv(128).decode("utf-8")
    data += tmp;

    validated = []

    msgs = data.split('\xff')
    data = msgs.pop()

    for msg in msgs:
        if msg[0] == '\x00':
            validated.append(msg[1:])

    for v in validated:
        print(v)
        conn.send('\x00' + v + '\xff')
    for i in range(17):
        conn.send( str.encode('Hello!'))

    conn.close()

while True:
    conn,addr = s.accept()
    print('{}:{} connected'.format(addr[0],addr[1]))

    start_new_thread(threaded_client, (conn,))
