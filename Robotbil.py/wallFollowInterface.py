class WallFollowInterface:
    def __init__(self, wall_follow_logic):
        self.wall_follow_logic = wall_follow_logic

    def start_wall_follow(self):
        print("Starting Wall Follow...")
        self.wall_follow_logic.start()

    def stop_wall_follow(self):
        print("Stopping Wall Follow...")
        self.wall_follow_logic.stop()

    def get_current_distance(self):
        distance = self.wall_follow_logic.get_distance()
        print(f"Current distance to wall: {distance} cm")


# Simulering af wall-follow-logik
class WallFollowLogic:
    def start(self):
        print("Wall following initiated.")

    def stop(self):
        print("Wall following stopped.")

    def get_distance(self):
        # Simulerer en måling fra en ToF-sensor
        return 15.2  # Eksempelværdi


# Eksempel på brug af WallFollowInterface-klassen
if __name__ == "__main__":
    logic = WallFollowLogic()
    interface = WallFollowInterface(logic)

    interface.start_wall_follow()
    interface.get_current_distance()
    interface.stop_wall_follow()
