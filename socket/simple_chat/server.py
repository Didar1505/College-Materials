import socket
import threading

clients = []
lock = threading.Lock()

def broadcast(message):
    with lock:
        for client in clients:
            try:
                client.sendall((message + "\n").encode())
            except OSError:
                pass

def handle(client):
    name = ""

    try:
        reader = client.makefile("r", encoding="utf-8")
        name = reader.readline().strip()

        if not name:
            return

        with lock:
            clients.append(client)

        broadcast(f"{name} joined the chat")

        for message in reader:
            message = message.strip()

            if message == "/quit":
                break

            if message:
                broadcast(f"{name}: {message}")

    except (OSError, UnicodeError):
        pass

    finally:
        with lock:
            if client in clients:
                clients.remove(client)

        client.close()

        if name:
            broadcast(f"{name} left the chat")


server = socket.socket()
server.bind(("0.0.0.0", 5000))
server.listen()

print("Chat server started!")

while True:
    client, address = server.accept()
    print("Connected:", address)

    thread = threading.Thread(target=handle, args=(client,))
    thread.start()
