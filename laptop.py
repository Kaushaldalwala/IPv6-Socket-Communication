import socket

def start_server():
    # Create an IPv6 socket
    server_socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    
    # Allow reuse of address
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # Bind to IPv6 address and port (use '::' for all interfaces)
    server_address = ('::', 12345)
    server_socket.bind(server_address)
    
    # Listen for incoming connections
    server_socket.listen(1)
    print("Server is listening on port 12345...")
    
    try:
        while True:
            # Accept client connection
            client_socket, client_address = server_socket.accept()
            print(f"Connected to client: {client_address}")
            
            # Get text input from user
            message = input("Enter text to send (or 'exit' to quit): ")
            if message.lower() == 'exit':
                break
                
            # Send text to client
            client_socket.sendall(message.encode('utf-8'))
            print("Text sent to client.")
            
            # Close the client socket
            client_socket.close()
    
    except KeyboardInterrupt:
        print("\nServer shutting down...")
    finally:
        server_socket.close()

if __name__ == "__main__":
    start_server()