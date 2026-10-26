import socket
import os

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5001

def list_files():
    s = socket.socket()
    s.connect((SERVER_HOST, SERVER_PORT))
    s.send(b"LIST")
    
    response = s.recv(4096).decode()
    _, files = response.split('|')

    if files == "(empty)":
        print("[ ] No files on server.")
    else:
        print("[Server Files]")
        for f in files.split(','):
            print(" •", f)

    s.close()


def upload(filepath):
    filename = os.path.basename(filepath)
    filesize = os.path.getsize(filepath)

    s = socket.socket()
    s.connect((SERVER_HOST, SERVER_PORT))
    s.send(f"UPLOAD|{filename}|{filesize}".encode())
    s.recv(2)

    with open(filepath, "rb") as f:
        while chunk := f.read(4096):
            s.sendall(chunk)

    s.close()
    print(f"[✓] Uploaded '{filename}'")

def download(filename):
    s = socket.socket()
    s.connect((SERVER_HOST, SERVER_PORT))
    s.send(f"DOWNLOAD|{filename}".encode())

    response = s.recv(1024).decode()

    if response.startswith("ERR"):
        print(response)
        s.close()
        return

    _, filesize = response.split('|')
    filesize = int(filesize)

    received = 0
    with open(filename, "wb") as f:
        while received < filesize:
            chunk = s.recv(4096)
            if not chunk:
                break
            f.write(chunk)
            received += len(chunk)

    s.close()
    print(f"[↓] Downloaded '{filename}' ({filesize} bytes)")

if __name__ == "__main__":
    print("Choose action:")
    print("1) Upload file")
    print("2) Download file")
    print("3) List files on server")
    choice = input("> ")

    if choice == "1":
        filepath = input("Enter file path to upload: ")
        upload(filepath)

    elif choice == "2":
        filename = input("Enter file name to download: ")
        download(filename)

    elif choice == '3':
        list_files()
