import http.server
import socketserver
import time

# Configurations
PORT = 8080
RATE_LIMIT = 5  # requests per IP within TIME_FRAME seconds
TIME_FRAME = 10  # seconds

# Tracking requests per IP address
request_counts = {}


class RateLimitingHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        client_ip = self.client_address[0]
        current_time = time.time()

        # Check if IP is in request_counts and update its count
        if client_ip in request_counts:
            # Remove old requests beyond the time frame
            request_counts[client_ip] = [t for t in request_counts[client_ip] if t > current_time - TIME_FRAME]
            request_counts[client_ip].append(current_time)
        else:
            request_counts[client_ip] = [current_time]

        # Enforce rate limit
        if len(request_counts[client_ip]) > RATE_LIMIT:
            self.send_response(429)
            self.end_headers()
            self.wfile.write(b"429 Too Many Requests - Rate limit exceeded")
        else:
            # Proceed with normal request handling
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Hello! You are within the rate limit.")


with socketserver.TCPServer(("", PORT), RateLimitingHandler) as httpd:
    print(f"Rate-limited server serving on port {PORT}")
    httpd.serve_forever()
