import socket
import time

host, port = "127.0.0.1", 25001
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))
flag = True
sendingData = "12,1,2,3" #Vector3   x = 0, y = 0, z = 0
while flag:
     sendingData = "dio,1,2,6"
     sock.sendall(sendingData.encode("UTF-8")) #Converting string to Byte, and sending it to C#
     receivedData = sock.recv(1024).decode("UTF-8") #receiveing data in Byte fron C#, and convert
     print(receivedData)
     if receivedData:
        flag = False
