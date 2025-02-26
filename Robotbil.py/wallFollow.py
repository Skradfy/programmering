class WallFollow:
    def getDistance(self):
        # Simulerer en måling fra en sensor
        return 15.2  # Eksempelafstand

# Eksempel på brug af WallFollow
if __name__ == "__main__":
    wall_follow = WallFollow()
    print(f"Distance to wall: {wall_follow.getDistance()} cm")
