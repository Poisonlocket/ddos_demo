# This will start a simple HTTP server on port 8080
import http.server
import socketserver

PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("localhost", PORT), Handler) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()
