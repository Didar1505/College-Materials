import socket
import threading
import os

HOST = '0.0.0.0'
PORT = 5001

def handle_client(conn, addr):
    print(f"[+] Connection from {addr}")

    request = conn.recv(1024).decode().strip()
    parts = request.split('|')

    command = parts[0]

    # Ensure upload folder exists
    os.makedirs("uploads", exist_ok=True)

    if command == "UPLOAD":
        filename = parts[1]
        filesize = int(parts[2])

        conn.send(b"OK")

        filepath = os.path.join("uploads", filename)
        received = 0
        with open(filepath, "wb") as f:
            while received < filesize:
                chunk = conn.recv(4096)
                if not chunk:
                    break
                f.write(chunk)
                received += len(chunk)

        print(f"[✓] Uploaded '{filename}'")
        conn.close()

    elif command == "DOWNLOAD":
        filename = parts[1]
        filepath = os.path.join("uploads", filename)

        if not os.path.exists(filepath):
            conn.send(b"ERR|File not found")
            conn.close()
            return

        filesize = os.path.getsize(filepath)
        conn.send(f"OK|{filesize}".encode())

        with open(filepath, "rb") as f:
            while True:
                chunk = f.read(4096)
                if not chunk:
                    break
                conn.sendall(chunk)

        print(f"[↓] Sent '{filename}' to {addr}")
        conn.close()

    elif command == "LIST":
        files = os.listdir("uploads")
        if files:
            conn.send(f"FILELIST|{','.join(files)}".encode())
        else:
            conn.send(b"FILELIST|(empty)")
        conn.close()


def main():
    server = socket.socket()
    server.bind((HOST, PORT))
    server.listen()

    print(f"[SERVER] Listening on {HOST}:{PORT}")

    while True:
        conn, addr = server.accept()
        threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()

if __name__ == "__main__":
    threading.Thread(target=main, daemon=True).start()
    input("Press Enter to exit")
