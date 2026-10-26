
import socket
import random

number = random.randint(1, 100)

server = socket.socket()
server.bind(("0.0.0.0", 5000))
server.listen()

print("Сервер запущен!")

while True:
    client, address = server.accept()

    guess = int(client.recv(1024).decode())
    print(address, "предположил:", guess)

    if guess < number:
        answer = "Больше"
    elif guess > number:
        answer = "Меньше"
    else:
        answer = "Победа!"
        number = random.randint(1, 100)

    client.sendall(answer.encode())
    client.close()
