
from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        page = """
        <html>
        <body>
            <h2>Student Login</h2>

            <form method="POST" action="/login">
                Username: <input name="username"><br><br>
                Password: <input name="password" type="password"><br><br>
                <button type="submit">Login</button>
            </form>
        </body>
        </html>
        """

        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(page.encode())

    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        data = self.rfile.read(length)

        print("Received data:", data.decode())

        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(b"Login request received!")


server = HTTPServer(("127.0.0.1", 8000), Handler)

print("Server running at http://127.0.0.1:8000")

server.serve_forever()
