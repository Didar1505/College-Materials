
import socket

while True:
    number = input("Угадай число (1-100): ")

    client = socket.socket()
    client.connect(("192.168.1.10", 5000))

    client.sendall(number.encode())

    answer = client.recv(1024).decode()
    print("Сервер:", answer)

    client.close()

    if answer == "Победа!":
        break
