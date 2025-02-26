import tkinter as tk

class UserInterface:
    def __init__(self, master):
        self.master = master
        master.title("Robot Control Panel")

        self.label = tk.Label(master, text="Robot Control")
        self.label.pack()

        # Knapper til motorstyring
        self.forward_button = tk.Button(master, text="Forward", command=self.move_forward)
        self.forward_button.pack()

        self.backward_button = tk.Button(master, text="Backward", command=self.move_backward)
        self.backward_button.pack()

        self.left_button = tk.Button(master, text="Left", command=self.move_left)
        self.left_button.pack()

        self.right_button = tk.Button(master, text="Right", command=self.move_right)
        self.right_button.pack()

        self.stop_button = tk.Button(master, text="Stop", command=self.stop)
        self.stop_button.pack()

        # Label for batteristatus
        self.battery_label = tk.Label(master, text="Battery: Checking...")
        self.battery_label.pack()

        # Knap til at opdatere batteristatus
        self.update_battery_button = tk.Button(master, text="Update Battery", command=self.update_battery_status)
        self.update_battery_button.pack()

    def move_forward(self):
        print("Moving Forward")

    def move_backward(self):
        print("Moving Backward")

    def move_left(self):
        print("Turning Left")

    def move_right(self):
        print("Turning Right")

    def stop(self):
        print("Stopping")

    def update_battery_status(self):
        # Simulerer opdatering af batteristatus (her kan du integrere dit powerManagement modul)
        self.battery_label.config(text="Battery: 7.2V")

if __name__ == "__main__":
    root = tk.Tk()
    gui = UserInterface(root)
    root.mainloop()
