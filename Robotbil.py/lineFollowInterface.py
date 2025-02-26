class LineFollowInterface:
    def __init__(self, line_follow):
        self.line_follow = line_follow

    def start(self):
        print("Starting line-follow mode...")
        print(f"Reflection value: {self.line_follow.getReflection()}")

    def stop(self):
        print("Stopping line-follow mode.")

# Eksempel på brug af LineFollowInterface
if __name__ == "__main__":
    line_follow = LineFollow()
    interface = LineFollowInterface(line_follow)
    interface.start()
    interface.stop()
