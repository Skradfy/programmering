import socket

# Define Pico's IP address and port
pico_ip = "192.168.1.47"  # Replace with your Pico's IP address
pico_port = 5005

# Create a UDP client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def send_command(command):
    try:
        # Send command to the Pico
        client_socket.sendto(command.encode(), (pico_ip, pico_port))
        
        # Receive and print the response from the Pico
        response, addr = client_socket.recvfrom(1024)
        print("Response from Pico:", response.decode())
    except Exception as e:
        print(f"Failed to send command: {e}")

# Menu function to display options and send commands
def menu():
    while True:
        print("\nLED Control Menu")
        print("1. Turn LED1 ON")
        print("2. Turn LED1 OFF")
        print("3. Turn LED2 ON")
        print("4. Turn LED2 OFF")
        print("5. Turn LED3 ON")
        print("6. Turn LED3 OFF")
        print("7. Turn LED4 ON")
        print("8. Turn LED4 OFF")
        print("9. Turn LED5 ON")
        print("10. Turn LED5 OFF")
        print("11. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            send_command("LED1 ON")
        elif choice == "2":
            send_command("LED1 OFF")
        elif choice == "3":
            send_command("LED2 ON")
        elif choice == "4":
            send_command("LED2 OFF")
        elif choice == "5":
            send_command("LED3 ON")
        elif choice == "6":
            send_command("LED3 OFF")
        elif choice == "7":
            send_command("LED4 ON")
        elif choice == "8":
            send_command("LED4 OFF")
        elif choice == "9":
            send_command("LED5 ON")
        elif choice == "10":
            send_command("LED5 OFF")
        elif choice == "11":
            print("Exiting the menu.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
