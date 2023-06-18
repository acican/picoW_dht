import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the host and port
host = '127.0.0.1'
port = 12345

# Bind the socket to the host and port
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen(1)

print("Server listening on {}:{}".format(host, port))

# Accept a client connection
client_socket, address = server_socket.accept()
print("Connected to client:", address)

# Receive data from the client
data = client_socket.recv(1024).decode()
print("Received data:", data)

# Send a response back to the client
response = "Hello from the server!"
client_socket.send(response.encode())

# Close the connection
client_socket.close()
server_socket.close()
