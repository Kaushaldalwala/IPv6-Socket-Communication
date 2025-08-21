import socket

def start_client():
    # Create an IPv6 socket
    client_socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    
    # Server IPv6 address and port
    server_ipv6_address = 'your_ipv6_address'  # Laptop's IPv6 address
    server_address = (server_ipv6_address, 12345)
    
    try:
        # Connect to the server
        client_socket.connect(server_address)
        print(f"Connected to server: {server_address}")
        
        # Receive text (buffer size = 1024 bytes)
        data = client_socket.recv(1024)
        print(f"Received text: {data.decode('utf-8')}")
    
    except Exception as e:
        print(f"Error: {e}")
    
    finally:
        # Close the socket
        client_socket.close()

if __name__ == "__main__":
    start_client()