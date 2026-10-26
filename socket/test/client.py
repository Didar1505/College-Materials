import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 12000))
print("connected to the server")

file_path = 'downloaded/test.txt'
file = open(file_path, 'wb')

while True:
    data = client.recv(1024)
    file.write(data)
    if not data: break
file.close()
client.close()
print("Downloaded file")