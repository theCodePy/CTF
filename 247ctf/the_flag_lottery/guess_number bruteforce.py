import socket
import random
import time


s_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s_client.connect(("4dda224144efb1c5.247ctf.com",50420))
secret = random.Random()
secret.seed(int(time.time()))
my_choice = round(secret.random(), 12)
data = s_client.recv(1024)
print(data)
s_client.send(f"{my_choice}".encode())
data = s_client.recv(1024)
print("mychoice=",my_choice)
print(data)
s_client.close()