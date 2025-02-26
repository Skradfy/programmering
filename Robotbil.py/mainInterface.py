class MainInterface:
    def __init__(self):
        print("Main Interface Initialized")

    def start(self):
        print("Starting the robot...")

    def stop(self):
        print("Stopping the robot...")

# Eksempel på brug af MainInterface
if __name__ == "__main__":
    interface = MainInterface()
    interface.start()
