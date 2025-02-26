class RemoteControl:
    def send_command(self, command):
        print(f"Command sent: {command}")

# Eksempel på brug af RemoteControl
if __name__ == "__main__":
    remote = RemoteControl()
    remote.send_command("MOVE_FORWARD")
