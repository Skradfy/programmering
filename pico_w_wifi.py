import socket

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.bind(('', 12345))

while True:
    data, addr = udp_socket.recvfrom(5005)  # Buffer size
    print(f"Received message: {data.decode()} from {addr}")
