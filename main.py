import network
import socket
import time
import struct
import dht

from machine import Pin

sensor = dht.DHT22(Pin(20))

ssid = 'ssid'
password = 'password'

host = ''
 
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

# Wait for connect or fail
max_wait = 10
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print('waiting for connection...')
    time.sleep(1)

# Handle connection error
if wlan.status() != 3:
    raise RuntimeError('network connection failed')
else:
    print('connected')
    status = wlan.ifconfig()
    host = status[0]
    print( 'ip = ' + host )
    
# Get the local machine's IP address
#host = socket.gethostname()
port = 12345  # Choose any free port number

# Open socket
#addr = socket.getaddrinfo(host, port)[0][-1]
#print("ip server: ", addr)

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the host and port
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen(1)
print("Server listening on {}:{}".format(host, port))

# Listen for connections
while True:
    try:
        client_socket, addr = server_socket.accept()
        print('client connected from', addr)

        request = client_socket.recv(1024)
        print(request)
        
        sensor.measure()
        temp = sensor.temperature()
        umid = sensor.humidity()
       
        response = str(temp) + "/" + str(umid)
        
        #cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        client_socket.send(response.encode())
        client_socket.close()
 
    except OSError as e:
        client_socket.close()
        print('connection closed')
