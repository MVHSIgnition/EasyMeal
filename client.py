from PIL import Image
import socket
import sys
import pickle

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = "35.163.41.116"
port = 5555

try:
    s.connect((server, port))
except socket.error as e:
    print(str(e))

image = s.recv(140000)

#image.decode()
image = Image.frombytes("RGB", (500,500), image)
image.save("%d.png" % 123, "PNG")
#with open("test.ppk", "wb") as f:
#    f.write(image)
    
