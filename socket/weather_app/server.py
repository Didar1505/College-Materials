import threading
import socket 
import pyowm
data = {
    'Moscow': [3, 4, -3, 5, 6, 8],
    'Stavropol': [3, 4, -3, 5, 6, 8],
    'Peterburg': [3, 4, -3, 5, 6, 8],
    'Kazan': [3, 4, -3, 5, 6, 8],
    'Minwod': [3, 4, -3, 5, 6, 8]
}

owm = pyowm.OWM('2f5f6064a2e7b417bb9d4ab541d12666')
mgr = owm.weather_manager()


def get_weather(city_name):
    try:
        observation = mgr.weather_at_place(city_name)
        w = observation.weather
        return w.temperature('celsius')['temp']
    except pyowm.commons.exceptions.NotFoundError:
        return -1

def handle_client(client:socket.socket):
    try:
        while True:
            message = client.recv(1024).decode().strip()
            print("From client:", message)

            if not message:
                break

            weather = get_weather(message)
            if weather == -1:
                break

            client.send(str(weather).encode())
    except:
        pass
    finally:
        print("Client disconnected")
        client.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    hostname = '127.0.0.1'
    port = 12000
    server.bind((hostname, port))
    server.listen(5)
    print("Сервер запущен на порту 12000...")

    while True:
        client, address = server.accept()
        print("Connected client with: ", address)
        threading.Thread(target=handle_client, args=(client,), daemon=True).start()


threading.Thread(target=main, daemon=True).start()
input('press enter to exit')
