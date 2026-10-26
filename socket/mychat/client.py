import socket
import threading

def handle_messages(client:socket.socket):
    while True:
        try:
            message = client.recv(1024).decode()
            if not message:
                break
            print(message)
        except:
            client.close()
            break

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("192.168.88.128", 55555))
    print("Connected to the server")

    threading.Thread(target=handle_messages, args=(client, ), daemon=True).start()
    
    while True:
        message = input("You: ")
        if message == 'exit':
            break
        client.send(message.encode())

    client.close()
main()
