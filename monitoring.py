import matplotlib.pyplot as plt
import requests
import threading

url = 'http://localhost:8080'
num_requests = 100
success_responses = 0
blocked_responses = 0
responses = []

def send_request():
    global success_responses, blocked_responses
    try:
        response = requests.get(url)
        if response.status_code == 200:
            success_responses += 1
        elif response.status_code == 429:
            blocked_responses += 1
        responses.append(response.status_code)
    except requests.exceptions.RequestException:
        responses.append(None)

threads = []
for _ in range(num_requests):
    thread = threading.Thread(target=send_request)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

# Visualize
labels = ['Success', 'Blocked']
values = [success_responses, blocked_responses]

plt.bar(labels, values, color=['green', 'red'])
plt.title("DDoS Defense Visualization")
plt.xlabel("Response Type")
plt.ylabel("Number of Requests")
plt.show()
