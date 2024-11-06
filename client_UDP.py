import socket

# Create a UDP socket
c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Specify the server address and port
server_address = ('localhost', 9999)

# Get the user's name
name = input("What is your name? ")

# Send the name to the server
c.sendto(bytes(name, 'utf-8'), server_address)

# Receive the response from the server
data, _ = c.recvfrom(1024)  # Receive up to 1024 bytes
print(data.decode())
