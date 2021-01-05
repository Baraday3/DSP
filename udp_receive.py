import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
address =("192.168.1.10",8888)
sock.bind(address)
print("Baglanti Kuruldu")

while True:
   data=sock.recv(1024)
   print(data)
  

#sudo ifconfig eth0 192.168.1.10 netmask 255.255.255.0

