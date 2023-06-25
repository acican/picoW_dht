import tkinter as tk
import socket
import sys

from datetime import datetime

# Define the host and port
host = 'PicoW'
port = 12345
remote_ip = '192.168.1.3'

def read_data():
    # Create a socket object
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error:
        print('Failed to create socket')
        sys.exit()

    # Connect to remote server
    print('# Connecting to server, ' + host + ' (' + remote_ip + ')')

    try:
        client_socket.connect((remote_ip, port))
        print('Connected to server:', host, port)
    except socket.error:
        print('Failed to connect server')
        sys.exit()

    # Send data to the server
    data = "Hello from the client!"
    client_socket.send(data.encode())

    # Receive the server's response
    response = client_socket.recv(1024).decode()
    print("Server's response:", response)

    # Close the connection
    client_socket.close()
    return response

def update_date():
    dat = read_data()
    arr_dat = dat.split("/")
    print(arr_dat)
    entry_temp_text.set(arr_dat[0])
    entry_humid_text.set(arr_dat[1])
    
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    datetime_label.config(text=current_datetime)
    
    datetime_label.after(5000, update_date)  # Update every 1 second (1000 milliseconds)

# Create the main window
window = tk.Tk()

# Set the window title
window.title("Client dht (socket)")

# Set the window size
window.geometry("400x300")  # Width x Height in pixels

# Create label date
datetime_label = tk.Label(window, text="Data:")
datetime_label.pack()

# Create an entry widget
#entry1 = tk.Entry(window)
#entry1.pack()

# Create label temp
label2 = tk.Label(window, text="Temperatura (C) :")
label2.pack()

# Create entry temp
entry_temp_text = tk.StringVar()
entry_temp = tk.Entry(window, textvariable=entry_temp_text, justify="right")
entry_temp.pack()

# Create label humid
label3 = tk.Label(window, text="Umiditate (%) :")
label3.pack()

# Create entry humid
entry_humid_text = tk.StringVar()
entry_humid = tk.Entry(window, textvariable=entry_humid_text, justify="right")
entry_humid.pack()

# Update the date and time initially and start updating it periodically
update_date()

# Run the main window event loop
window.mainloop()
