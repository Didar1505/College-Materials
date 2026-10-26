import socket
import threading

connections = []

def broadcast(message, client):
    for conn in connections:
        if client != conn:
            conn.send(message)

def remove_client(client:socket.socket):
    if client in connections:
        client.close()
        connections.remove(client)

def handle(client:socket.socket, address):
    try:
        while True:
            message = client.recv(1024)
            if message:
                message_send = f"From {address}: {message.decode()}"
                print(message_send)
                broadcast(message_send.encode(), client)
            else:
                remove_client(client)
                break
    except Exception as e:
        print(e)
        print(f"Client {address} left the chat")
        remove_client(client)

def main():
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(("0.0.0.0", 55555))
        server.listen(10)
        print("Server started")

        while True:
            client, address = server.accept()
            connections.append(client)
            print(f"Client with {address} connected to the server")
            threading.Thread(target=handle, args=(client,address,), daemon=True).start()
        
    except Exception as e:
        print(e)
    finally:
        print(e)
        if len(connections) > 0:
            for conn in connections:
                remove_client(conn)
        server.close()

if __name__  == "__main__":
    threading.Thread(target=main, daemon=True).start()
    input("Press Enter to exit")
