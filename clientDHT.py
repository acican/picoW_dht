import tkinter as tk
import socket
import sys

# Create a socket object
try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print('Failed to create socket')
    sys.exit()

# Define the host and port
host = 'PicoW'
port = 12345

try:
    remote_ip = socket.gethostbyname(host)
except socket.gaierror:
    print('Hostname could not be resolved. Exiting')
    sys.exit()

# Connect to remote server
print('# Connecting to server, ' + host + ' (' + remote_ip + ')')
s.connect((remote_ip , port))    

# Connect to the server
try:
    client_socket.connect((host, port))
    print('Connected to server:', host, port)
except socket.error:
    print('Failed to cconnect server')
    sys.exit()

# Send data to the server
data = "Hello from the client!"
client_socket.send(data.encode())

# Receive the server's response
response = client_socket.recv(1024).decode()
print("Server's response:", response)

# Close the connection
client_socket.close()    

# Create the main window
window = tk.Tk()

# Set the window title
window.title("Client dht (socket)")

# Set the window size
window.geometry("400x300")  # Width x Height in pixels

# Create a label widget
label1 = tk.Label(window, text="Data:")
label1.pack()

# Create an entry widget
entry1 = tk.Entry(window)
entry1.pack()

# Create another label widget
label2 = tk.Label(window, text="Temperatura:")
label2.pack()

# Create another entry widget
entry2 = tk.Entry(window)
entry2.pack()

# Create another label widget
label3 = tk.Label(window, text="Umiditate:")
label3.pack()

# Create another entry widget
entry3 = tk.Entry(window)
entry3.pack()

# Run the main window event loop
window.mainloop()
