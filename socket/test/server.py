import socket

filename = 'test.txt'
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 12000))
server.listen(5)

file = open(filename, 'rb')
line = file.read(1024)

conn, adr = server.accept()
print("Started server")

while line:
    conn.send(line)
    line = file.read(1024)
file.close()
conn.close()
server.close()