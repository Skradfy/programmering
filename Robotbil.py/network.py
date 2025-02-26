import socket

class Network:
    def __init__(self, ip='192.168.0.10', port=8888):
        self.server_address = (ip, port)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def send_command(self, command):
        try:
            print(f"Sending command: {command}")
            self.sock.sendto(command.encode(), self.server_address)
        except Exception as e:
            print(f"Failed to send command: {e}")

    def close_connection(self):
        self.sock.close()

# Eksempel på at bruge Network-klassen
if __name__ == "__main__":
    network = Network()
    network.send_command("MOVE_FORWARD")
    network.close_connection()
