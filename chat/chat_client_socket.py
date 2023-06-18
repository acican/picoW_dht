import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the host and port
host = '127.0.0.1'
port = 12345

# Connect to the server
client_socket.connect((host, port))
print("Connected to server:", host, port)

# Send data to the server
data = "Hello from the client!"
client_socket.send(data.encode())

# Receive the server's response
response = client_socket.recv(1024).decode()
print("Server's response:", response)

# Close the connection
client_socket.close()
