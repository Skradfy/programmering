class MotorController:
    def robotMoveLogic(self, direction):
        if direction == "forward":
            print("Moving forward")
        elif direction == "backward":
            print("Moving backward")
        elif direction == "left":
            print("Turning left")
        elif direction == "right":
            print("Turning right")
        else:
            print("Stopping the robot")


# Eksempel på brug af MotorController
if __name__ == "__main__":
    motor = MotorController()
    motor.robotMoveLogic("forward")
