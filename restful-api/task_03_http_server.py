#!/usr/bin/python3
import http.server
import json


class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    # Handle GET requests
    def do_GET(self):

        # Root endpoint "/"
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
            return

        # /data endpoint -> return JSON
        elif self.path == "/data":
            payload = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(payload).encode())
            return

        # /status endpoint
        elif self.path == "/status":
            payload = {"status": "OK"}

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(payload).encode())
            return

        # Undefined endpoints → 404
        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            error_message = {"error": "Endpoint not found"}
            self.wfile.write(json.dumps(error_message).encode())


# Start server
if __name__ == "__main__":
    server_address = ("", 8000)   # localhost:8000
    httpd = http.server.HTTPServer(server_address, SimpleAPIHandler)
    print("Server running at http://localhost:8000")
    httpd.serve_forever()
