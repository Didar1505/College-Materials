import threading
import socket
import sys

SERVER_ADDRESS = input("ip: ")
LISTENING_PORT = int(input('port: '))
nickname = input("Nickname: ")

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
            
            else:
                print("Error ocurred during retrieving message")
                client.close()

        except Exception as e:
            print(f'Error handling message from server: {e}')
            client.close()
            break

def main():
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((SERVER_ADDRESS, LISTENING_PORT))

        threading.Thread(target=handle_messages, args=(client,), daemon=True).start()

        print('Connected to the chat!')

        while True:
            message = input(f"You: ")
            message_send = f"{nickname}: {message}"
            if message == 'quit':
                break
            client.send(message_send.encode())

        client.close()
    except Exception as e:
        print(f'Error connecting to server socket {e}')
        client.close()

if __name__ == '__main__':
    main()