import socket


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 12000))
print("Connected to the server")
while True:
    user_input = input("Write your query: ")
    if user_input == "exit":
        break
    try:
        client.send(user_input.encode())
        response = client.recv(1024).decode()
        print("Server:", response)
    except:
        print("error ocurred")
        break

client.close()