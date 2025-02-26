import network
import socket
import time
from machine import Pin

# Set up Wi-Fi connection
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

# Set static IP address (IP, Subnet Mask, Gateway, DNS)
wlan.ifconfig(('192.168.1.47', '255.255.255.0', '192.168.1.1', '8.8.8.8'))  # Replace with appropriate static IP settings

wlan.connect('WifiB100', 'g1bd96e76')

# Wait for the Wi-Fi connection to establish
while not wlan.isconnected() and wlan.status() >= 0:
    print("Waiting to connect...")
    time.sleep(1)

print("Connected to network:", wlan.ifconfig())  # Display the Pico's IP address
time.sleep(1)

# Set up UDP server
UDPServerSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
UDPServerSocket.bind(('0.0.0.0', 5005))  # Bind to all available IP addresses on port 5005
UDPServerSocket.setblocking(False)  # Set the socket to non-blocking mode
bufferSize = 1024

print("UDP Server started. Waiting for data...")

# Set up LEDs on GPIO 4, 5, 6, 7, 8
leds = {
    "LED1": Pin(4, Pin.OUT),  # LED1 on GPIO 4
    "LED2": Pin(5, Pin.OUT),  # LED2 on GPIO 5
    "LED3": Pin(6, Pin.OUT),  # LED3 on GPIO 6
    "LED4": Pin(7, Pin.OUT),  # LED4 on GPIO 7
    "LED5": Pin(8, Pin.OUT)   # LED5 on GPIO 8
}

# Function to control LEDs based on the received command
def control_leds(command):
    led_name, action = command.split()  # Split command into LED name and action
    if led_name in leds and action in ["ON", "OFF"]:
        leds[led_name].value(1 if action == "ON" else 0)
        print(f"{led_name} turned {action}")
    else:
        print(f"Unknown command: {command}")

# Non-blocking UDP server loop
while True:
    try:
        data, addr = UDPServerSocket.recvfrom(bufferSize)
        if data:
            message = data.decode().strip()  # Decode the message
            print(f"Received message: {message} from {addr}")

            # Control the LEDs based on the received message
            control_leds(message)

            # Send a response back to the client
            response = f"Executed command: {message}"
            UDPServerSocket.sendto(response.encode(), addr)
            print(f"Sent response to {addr}")
    except OSError as e:
        # If no data is received or any OSError occurs, just pass
        pass

    # Perform other tasks (e.g., you can add non-blocking checks here for other events)
    # Example: Check some sensor or perform other background tasks
    time.sleep(0.1)  # Avoid busy-waiting by adding a small sleep
