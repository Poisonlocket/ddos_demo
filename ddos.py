import requests
import threading

# URL to attack
url = 'http://localhost:8080'

# Number of requests to simulate
num_requests = 10000

def send_request():
    try:
        response = requests.get(url)
        print(f"Response code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

# Launch multiple threads to simulate multiple requests at once
threads = []
for request in range(num_requests):
    thread = threading.Thread(target=send_request)
    thread.start()
    threads.append(thread)

# Wait for all threads to complete
for thread in threads:
    thread.join()
