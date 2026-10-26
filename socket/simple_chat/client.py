
import socket
import threading

client = socket.socket()
client.connect(("192.168.1.10", 5000))

name = input("Your name: ")
client.sendall((name + "\n").encode())

def receive():
    try:
        for message in client.makefile("r", encoding="utf-8"):
            print("\n" + message.strip())
    except OSError:
        pass

thread = threading.Thread(target=receive, daemon=True)
thread.start()

print("Connected! Type /quit to exit.")

while True:
    try:
        message = input()

        client.sendall((message + "\n").encode())

        if message == "/quit":
            break

    except (OSError, EOFError, KeyboardInterrupt):
        break

client.close()
