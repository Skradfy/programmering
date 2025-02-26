import network
import time

# Configure your Wi-Fi SSID and password
SSID = 'WifiB100'
PASSWORD = 'g1bd96e76'

# Initialize the network interface
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)

# Wait for connection
max_wait = 10
while max_wait > 0:
    if wlan.isconnected():
        break
    print('Waiting for connection...')
    time.sleep(1)
    max_wait -= 1

# Check if connected and print the IP address
if wlan.isconnected():
    print('Connected successfully!')
    print('IP address:', wlan.ifconfig()[0])
else:
    print('Failed to connect to the network')
