from userInterfaceImprovements import UserInterface
from network import Network
import tkinter as tk

class RemoteInterface:
    def __init__(self, master):
        self.gui = UserInterface(master)
        self.network = Network()

        # Tilknyt knapperne til netværkskommandoer
        self.gui.forward_button.config(command=self.move_forward)
        self.gui.backward_button.config(command=self.move_backward)
        self.gui.left_button.config(command=self.move_left)
        self.gui.right_button.config(command=self.move_right)
        self.gui.stop_button.config(command=self.stop)

    def move_forward(self):
        print("Sending command to move forward")
        self.network.send_command("MOVE_FORWARD")

    def move_backward(self):
        print("Sending command to move backward")
        self.network.send_command("MOVE_BACKWARD")

    def move_left(self):
        print("Sending command to move left")
        self.network.send_command("MOVE_LEFT")

    def move_right(self):
        print("Sending command to move right")
        self.network.send_command("MOVE_RIGHT")

    def stop(self):
        print("Sending stop command")
        self.network.send_command("STOP")

    def update_battery_status(self):
        # Batteristatus kan også integreres her
        self.gui.update_battery_status()

# Eksempel på at køre RemoteInterface
if __name__ == "__main__":
    root = tk.Tk()
    remote_interface = RemoteInterface(root)
    root.mainloop()
