import socket 
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print('socket created')

s.bind(('localhost',9999))

print("Wait for connection")

while True:
    data,addr=s.recvfrom(1024)
    name=data.decode()
    print('the client is',name,addr)
    s.sendto(bytes("Welcome and hello",'utf-8'),addr)
  
