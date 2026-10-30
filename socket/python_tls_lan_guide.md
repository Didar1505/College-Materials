# Python TLS Server over a Local Network (LAN)

## Goal

This guide shows how to run a Python TCP server on a local network,
protect its traffic with TLS, let students connect from their computers,
and inspect the encrypted communication in Wireshark.

We use:

-   Python `socket` for TCP networking.
-   Python `ssl` for TLS encryption.
-   OpenSSL to create a classroom certificate.
-   Wireshark to inspect packets.
-   Windows PowerShell for network configuration.

**Important:** Do not encrypt each string manually. TLS protects the
whole connection. Your Python program still sends and receives ordinary
bytes; TLS encrypts and decrypts them underneath.

## 1. How it works

1.  TCP establishes a connection between the client and server.
2.  TLS authenticates the server and negotiates encryption keys.
3.  Application messages travel as encrypted TLS records.
4.  The server decrypts received data before passing it to Python.

Without TLS, Wireshark can read an ordinary message such as
`Hello, Server!`. With TLS, Wireshark normally sees encrypted
application records instead.

## 2. Find the server's private IP address

On the teacher's computer, open PowerShell:

``` powershell
ipconfig
```

Find the IPv4 address under the active Wi-Fi or Ethernet adapter. For
example:

``` text
IPv4 Address: 192.168.1.10
```

Replace `192.168.1.10` in this guide with the actual IP address of the
teacher's computer.

  Address          Meaning
  ---------------- -------------------------------------------------------
  `127.0.0.1`      Loopback; this computer itself
  `localhost`      Name that normally resolves to this computer
  `0.0.0.0`        Server bind address meaning all local IPv4 interfaces
  `192.168.1.10`   Example private LAN address

The server will bind to `0.0.0.0`. Students must connect to the
teacher's actual private IP address, not to `0.0.0.0`.

## 3. Generate a TLS certificate

TLS needs a server certificate and its corresponding private key.

For this classroom experiment, create a self-signed certificate with
OpenSSL. The certificate must contain the server's LAN IP in its
**Subject Alternative Name (SAN)**. Otherwise, the client will reject
the certificate when connecting by IP.

Check that OpenSSL is installed:

``` powershell
openssl version
```

In PowerShell, run the following command, replacing `192.168.1.10` with
the actual server IP:

``` powershell
openssl req -x509 -newkey rsa:2048 -keyout server.key -out server.crt -days 365 -nodes -subj "/CN=192.168.1.10" -addext "subjectAltName=IP:192.168.1.10,DNS:localhost,IP:127.0.0.1"
```

The command creates:

  -----------------------------------------------------------------------
  File                                Purpose
  ----------------------------------- -----------------------------------
  `server.crt`                        Public certificate. Give students a
                                      copy so their clients can verify
                                      the server.

  `server.key`                        Private key. Keep it on the server;
                                      never distribute it.
  -----------------------------------------------------------------------

### If using Git Bash

Git Bash may convert `/CN=...` into a Windows path. If that happens,
run:

``` bash
MSYS_NO_PATHCONV=1 openssl req -x509 -newkey rsa:2048 -keyout server.key -out server.crt -days 365 -nodes -subj "/CN=192.168.1.10" -addext "subjectAltName=IP:192.168.1.10,DNS:localhost,IP:127.0.0.1"
```

### Verify the certificate

``` powershell
openssl x509 -in server.crt -text -noout
```

Find `Subject Alternative Name`. It should include the IP used by
clients:

``` text
X509v3 Subject Alternative Name:
    IP Address:192.168.1.10, DNS:localhost, IP Address:127.0.0.1
```

**Security notes:**

-   A self-signed certificate is suitable for a controlled classroom
    demonstration.
-   The client trusts it because we explicitly provide it as a trusted
    certificate file.
-   The certificate must match the address used by the client.
-   Distribute `server.crt` only. Never distribute `server.key`.
-   The `-nodes` option creates an unencrypted private key file, so
    restrict access to it.
-   For a real public service, use a certificate issued by a trusted
    certificate authority.

## 4. Create the TLS server

Create `server.py` in the same directory as `server.crt` and
`server.key`.

This version uses a separate thread for each client, allowing several
students to connect without waiting for the previous connection to
finish.

``` python
import socket
import ssl
import threading

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain("server.crt", "server.key")


def handle_client(client, address):
    try:
        with context.wrap_socket(client, server_side=True) as secure_client:
            print("Secure connection from:", address)
            print("TLS version:", secure_client.version())
            print("Cipher:", secure_client.cipher())

            message = secure_client.recv(1024)

            if message:
                print("FROM", address, message.decode("utf-8"))

                secure_client.sendall(
                    "Message received!".encode("utf-8")
                )

    except (ssl.SSLError, OSError) as error:
        print("Connection error:", error)


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind(("0.0.0.0", 8080))
server.listen()

print("Secure server running on port 8080...")

while True:
    client, address = server.accept()

    thread = threading.Thread(
        target=handle_client,
        args=(client, address),
        daemon=True
    )
    thread.start()
```

Run it:

``` powershell
python server.py
```

Expected output:

``` text
Secure server running on port 8080...
```

### Important server code

  -------------------------------------------------------------------------------
  Code                                        Purpose
  ------------------------------------------- -----------------------------------
  `ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)`   Creates a TLS server context

  `load_cert_chain()`                         Loads the certificate and private
                                              key

  `wrap_socket()`                             Wraps a TCP socket with TLS

  `bind(("0.0.0.0", 8080))`                   Listens on all local IPv4
                                              interfaces on port 8080

  `listen()`                                  Starts accepting connections

  `accept()`                                  Accepts an incoming client

  `threading.Thread()`                        Handles a client in a separate
                                              thread

  `recv(1024)`                                Reads up to 1024 bytes

  `sendall()`                                 Sends the response through TLS
  -------------------------------------------------------------------------------

This example reads one short message per connection. `recv(1024)` means
"read up to 1024 bytes"; it does not guarantee that a complete
application message always arrives in one call. A production protocol
should define message boundaries and handle partial reads.

## 5. Create the TLS client

Create `client.py`. Students need a copy of `server.crt` in the same
directory. They do not need the server's private key.

``` python
import socket
import ssl

SERVER_IP = "192.168.1.10"
PORT = 8080

context = ssl.create_default_context(cafile="server.crt")

client = socket.create_connection((SERVER_IP, PORT))

with context.wrap_socket(
    client,
    server_hostname=SERVER_IP
) as secure_client:

    print("Connected using:", secure_client.version())
    print("Cipher:", secure_client.cipher())

    message = input("Enter message: ")

    secure_client.sendall(message.encode("utf-8"))

    response = secure_client.recv(1024).decode("utf-8")

    print("Server:", response)
```

Replace `192.168.1.10` with the teacher's actual LAN IP address.

Run:

``` powershell
python client.py
```

Example output:

``` text
Connected using: TLSv1.3
Cipher: ('TLS_AES_256_GCM_SHA384', 'TLSv1.3', 256)
Enter message: Hello, Server!
Server: Message received!
```

The actual TLS version and cipher suite depend on the Python/OpenSSL
versions and the algorithms supported by both sides.

### How certificate verification works

``` python
context = ssl.create_default_context(cafile="server.crt")
```

This tells the client to trust the supplied certificate.

``` python
server_hostname=SERVER_IP
```

This enables identity verification against the IP address in the
certificate's SAN.

Do not disable certificate verification with `CERT_NONE` or
`check_hostname = False`. Encryption without server authentication can
leave the connection vulnerable to a man-in-the-middle attack.

## 6. Allow incoming connections through Windows Firewall

Windows Firewall may block incoming connections.

Open PowerShell **as Administrator**:

``` powershell
New-NetFirewallRule -DisplayName "Python TLS Server" -Direction Inbound -Protocol TCP -LocalPort 8080 -Action Allow -Profile Private
```

Check the active network profile:

``` powershell
Get-NetConnectionProfile
```

This firewall rule applies to networks classified as Private. Only use
the Private profile on a trusted network. Do not change an untrusted
public Wi-Fi network to Private just to make the demonstration work.

To remove the rule after the lesson:

``` powershell
Remove-NetFirewallRule -DisplayName "Python TLS Server"
```

## 7. Test connectivity from a student's computer

Before running the Python client, test whether the student's computer
can reach the server.

On the student's computer:

``` powershell
Test-NetConnection 192.168.1.10 -Port 8080
```

A successful result should include:

``` text
TcpTestSucceeded : True
```

If it returns `False`, check:

1.  Both computers are connected to a reachable LAN.
2.  The server is running.
3.  The server is listening on `0.0.0.0`, not only `127.0.0.1`.
4.  Windows Firewall allows inbound TCP port `8080`.
5.  The Wi-Fi network does not enable client/AP isolation.
6.  The client uses the correct server IP address and port.

A successful TCP test confirms that the port is reachable. It does not
prove that TLS certificate verification will succeed.

## 8. Inspect encrypted traffic in Wireshark

On the teacher's computer:

1.  Open Wireshark.
2.  Select the active Wi-Fi or Ethernet interface.
3.  Start capturing.
4.  Run the Python TLS server.
5.  Ask students to run their clients.
6.  Send test messages.

Use this display filter:

``` wireshark
tcp.port == 8080
```

### Useful filters

  Filter                      Purpose
  --------------------------- -------------------------------------
  `tcp.port == 8080`          All TCP traffic involving port 8080
  `tcp.flags.syn == 1`        TCP SYN packets
  `tls`                       Packets decoded as TLS
  `tls.handshake.type == 1`   TLS Client Hello
  `tls.handshake.type == 2`   TLS Server Hello
  `tls.app_data`              TLS application data records
  `tcp.flags.fin == 1`        TCP connection termination

### What to observe

The approximate sequence is:

1.  TCP SYN.
2.  TCP SYN, ACK.
3.  TCP ACK.
4.  TLS Client Hello.
5.  TLS Server Hello.
6.  Remaining TLS handshake messages.
7.  Encrypted TLS Application Data.
8.  TLS shutdown notification, when sent.
9.  TCP connection termination.

Some TLS handshake messages are encrypted in TLS 1.3. Without session
secrets, Wireshark may not display the certificate and later handshake
messages as readable fields.

### Compare HTTP and HTTPS

With the original unencrypted TCP server, Wireshark could show:

``` text
Hello, Server!
```

With TLS, Wireshark should show encrypted TLS records instead of the
original application message.

  Information                               Normally visible?
  ----------------------------------------- ---------------------------------
  Source IP address                         Yes
  Destination IP address                    Yes
  Source and destination ports              Yes
  Packet sizes and timing                   Yes
  TLS version and some handshake metadata   Partially
  Application message                       No, not without decryption keys
  Original message content                  No, not without decryption keys

TLS protects the content and integrity of data in transit. It does not
hide all network metadata and does not protect a compromised endpoint.

## 9. Classroom experiment

Suggested demonstration:

1.  Start the TLS server on the teacher's computer.
2.  Start Wireshark on the teacher's computer.
3.  Ask Student 1 to connect and send `Hello from Student 1!`.
4.  Ask Student 2 to connect and send `Hello from Student 2!`.
5.  Ask Student 3 to connect and send `Hello from Student 3!`.
6.  Observe the separate TCP connections and TLS handshakes.
7.  Find the encrypted application data records.
8.  Compare the result with the previous unencrypted TCP experiment.

Questions for students:

-   Can we identify the IP address of each client?
-   Can we identify the server port?
-   Can we read the original messages?
-   Why can the server read the messages while Wireshark cannot?
-   What is the purpose of the server certificate?
-   Why must the client verify the certificate?

**Expected result:** The Python server can read each original message
after TLS decrypts it. Wireshark can observe the network packets, but
cannot normally read the protected application content.

## 10. Troubleshooting

### `Connection refused`

Possible causes:

-   The server is not running.
-   The client uses the wrong IP or port.
-   The server is listening only on `localhost`.
-   The connection is blocked or rejected.

Check:

``` powershell
Test-NetConnection 192.168.1.10 -Port 8080
```

### `CERTIFICATE_VERIFY_FAILED`

Possible causes:

-   The client does not have the correct `server.crt`.
-   The certificate SAN does not contain the IP used by the client.
-   The certificate is incorrect or expired.
-   The client connects using a different hostname or IP than the
    certificate covers.

Regenerate the certificate with the correct LAN IP in the SAN,
distribute the new `server.crt`, and restart the server.

### OpenSSL subject name is interpreted as a Windows path

This can happen in Git Bash because MSYS converts arguments beginning
with `/` into Windows paths.

Use PowerShell, or run the command in Git Bash with:

``` bash
MSYS_NO_PATHCONV=1 openssl req ...
```

### Wireshark does not show TLS fields

Check that:

-   You selected the active network interface.
-   You are capturing the correct port.
-   The connection actually uses TLS.
-   The capture includes the beginning of the connection, including
    Client Hello.

## 11. Security recommendations

For this classroom experiment:

-   Use only a trusted local network.
-   Use fictional test messages, never real passwords.
-   Keep `server.key` on the server computer.
-   Distribute only `server.crt` to students.
-   Keep certificate verification enabled.
-   Do not configure router port forwarding.
-   Remove the temporary firewall rule after the lesson if it is no
    longer needed.
-   Remember that a self-signed certificate is a teaching setup, not a
    replacement for a properly managed public certificate.

The server is an educational example. It does not implement user
authentication, rate limiting, persistent storage or a production-grade
message-framing protocol.

## 12. Summary

  -----------------------------------------------------------------------
  Component                           Responsibility
  ----------------------------------- -----------------------------------
  `socket`                            Creates and manages TCP connections

  `ssl`                               Adds TLS encryption and certificate
                                      verification

  `threading`                         Allows the server to handle
                                      multiple clients concurrently

  `server.crt`                        Public certificate trusted by
                                      clients in this experiment

  `server.key`                        Server's private key

  Private LAN IP                      Address students use to reach the
                                      teacher's computer

  Port `8080`                         TCP port used by the educational
                                      service

  Windows Firewall                    Controls incoming connections

  Wireshark                           Captures and analyzes network
                                      traffic
  -----------------------------------------------------------------------

**Main takeaway:** TCP provides reliable transport, while TLS adds
confidentiality, integrity and server authentication. The Python
application continues to work with ordinary strings, but TLS protects
the bytes while they travel across the network.

### Official documentation

-   [Python `ssl` module](https://docs.python.org/3/library/ssl.html)
-   [Python `socket`
    module](https://docs.python.org/3/library/socket.html)
-   [Wireshark User's
    Guide](https://www.wireshark.org/docs/wsug_html_chunked/)
-   [OpenSSL documentation](https://docs.openssl.org/)
