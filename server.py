# This will start a simple HTTP server on port 8080
import http.server
import socketserver

PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("10.62.146.179", PORT), Handler) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()
