# URL Flooder

This script floods a target URL with spam messages by sending a specified number of requests with a specified delay between each request.

## Usage

### Prerequisites

- Python 3.x installed on your system.
- Required Python packages installed. You can install them using:

```
pip install -r requirements.txt

```

### Running the Script

1. Clone this repository or download the `url_flooder.py` file.
2. Open a terminal or command prompt.
3. Navigate to the directory containing `url_flooder.py`.
4. Run the script using the following command:



Replace `<url>` with the target URL to flood, `<count>` with the number of requests to send, and `<delay>` with the delay time between each request in seconds.

### Example

```
python url_flooder.py http://example.com/spam_endpoint 100 1.0

```


This command will send 100 spam messages to `http://example.com/spam_endpoint` with a delay of 1 second between each request.

## Arguments

- `url`: The target URL to flood.
- `count`: The number of requests to send.
- `delay`: The delay time between each request in seconds.

## Notes

- Ensure that you have permission to flood the target URL. Flooding a website without proper authorization may be illegal and unethical.
- Use this script responsibly and only for testing purposes on systems you own or have explicit permission to test.

## Disclaimer

The author of this script is not responsible for any misuse or damage caused by using this script. Use it at your own risk.
