import threading
import socket

connections = []
nicknames = []

def broadcast(message:str, connection:socket.socket):
    for conn in connections:
        if conn != connection:
            try:
                conn.send(message.encode())
            except Exception as e:
                print('Error broadcasting message: {e}')
                remove_conection(connection)

def remove_conection(connection:socket.socket):
    if connection in connections:
        index = connections.index(connection)
        connection.close()
        connections.remove(connection)

        nickname = nicknames[index]
        print(f"{nickname} has left the room")
        nicknames.remove(nickname)


def handle_user_connection(connection:socket.socket, address:str):
    while True:
        try:
            message = connection.recv(1024)

            if message:
                message_send = message.decode()
                print(message_send)
                broadcast(message_send, connection)
            else:
                remove_conection(connection)
                break
        except Exception as e:
            print(f'Error to handle user connection: {e}')
            remove_conection(connection)
            break

def recieve():
    LISTENING_PORT = 12000

    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('0.0.0.0', LISTENING_PORT))
        server.listen(5)
        print('Server running!')


        while True:
            con, adr = server.accept()
            con.send('NICK'.encode())
            nickname = con.recv(1024).decode()
            nicknames.append(nickname)
            print(f"{nickname} connected to the chat: {adr}")
            connections.append(con)
            threading.Thread(target=handle_user_connection, args=(con,adr,), daemon=True).start()

    except Exception as e:
        print(f'An error has occurred when instancing socket: {e}')
    finally:
        if len(connections) > 0:
            for con in connections:
                remove_conection(con)
            server.close()


if __name__ == "__main__":
    recieve_thread = threading.Thread(target=recieve, daemon=True)
    recieve_thread.start()
    input("Press Enter to exit!")
    