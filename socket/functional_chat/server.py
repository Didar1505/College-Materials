import socket
import threading
from weather import Weather
from quote import Quote

connections = []
nicknames = []

def broadcast(message, client=None):
    for conn in connections:
        if client != conn:
            conn.send(message)

def remove_client(client:socket.socket):
    if client in connections:
        index = connections.index(client)
        nick = nicknames[index]
        print(f"{nick} left the chat")
        nicknames.remove(nick)
        client.close()
        connections.remove(client)


def handle_command(raw, client:socket.socket):
    raw = raw.split()
    command = raw[0]
    if command == '/weather':
        temperature = Weather().get_weather(raw[1])
        response = f"The weather in {raw[1]} is {str(temperature)} temp"
        client.send(response.encode())
    if command == '/quote':
        response = Quote().get_random_quote()
        message_send = f'{response["quote"]} - {response['author']}'
        client.send(message_send.encode())


def handle(client:socket.socket):
    while True:
        try:
            message = client.recv(1024)
            if message:
                message = message.decode()
                if message.startswith("/"):
                    handle_command(message, client)
                else:
                    index = connections.index(client)
                    nick = nicknames[index]
                    message_send = f"{nick}: {message}"
                    print(message_send)
                    broadcast(message_send.encode(), client)
            else:
                remove_client(client)
        except Exception as e:
            print(f"Error to hande the connection: ", e)
            remove_client(client)
            break

def main():
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('0.0.0.0', 12000))
        server.listen(10)
        print("Server started listening on port:", 12000)


        while True:
            client, address = server.accept()
            client.send("NICK".encode())
            nick = client.recv(1024).decode()
            nicknames.append(nick)
            print(f"Connected {nick} with address: {address}")
            
            connections.append(client)
            threading.Thread(target=handle, args=(client,), daemon=True).start()


    except Exception as e:
        print("An error ocurred:",e)
    finally:
        if len(connections) > 0:
            for conn in connections:
                remove_client(conn)
        server.close()

if __name__ == '__main__':
    threading.Thread(target=main, daemon=True).start()
    input("Press Enter to exit! \n")