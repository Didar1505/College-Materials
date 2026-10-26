import socket
import sys
import threading
import random

nickname = f"User-{random.randint(1,100)}"

def handle_messages(client:socket.socket):
    while True:
        try:
            message = client.recv(1024)
            if message:
                if message.decode() == "NICK":
                    client.send(nickname.encode())
                else:
                    sys.stdout.write('\r' + ' ' * 80 + '\r')  # Clear line
                    print(message.decode())
                    sys.stdout.write("You: ")  # Reprint prompt
                    sys.stdout.flush()
        except Exception as e:
            print("Error occurred during connection:", e)
            client.close()
            break

def main():
    try:
        client  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(("127.0.0.1", 12000))
        print("Connected to the server!")
        threading.Thread(target=handle_messages, args=(client,)).start()

        while True:
            message = input("You: ")    
            if message == "quit":
                break
            client.send(message.encode())


    except Exception as e:
        print("Error ocurred with client: ", e)
    finally:
        client.close()
        print("connection closed")

main()