class RobotDiagnostics:
    def __init__(self, power_management, sensors, motors):
        self.power_management = power_management
        self.sensors = sensors
        self.motors = motors

    def check_power(self):
        voltage = self.power_management.read_voltage()
        current = self.power_management.read_current()
        if voltage < 6.5:  # Eksempelgrænse
            print(f"Warning: Low voltage detected: {voltage}V")
        else:
            print(f"Power status: Voltage: {voltage}V, Current: {current}A")

    def check_sensors(self):
        for sensor_name, sensor in self.sensors.items():
            sensor_status = sensor.test()
            print(f"{sensor_name} sensor status: {'OK' if sensor_status else 'Fail'}")

    def check_motors(self):
        motor_status = self.motors.test_motors()
        print(f"Motors diagnostic: {'All motors operational' if motor_status else 'Motor issue detected'}")

    def run_diagnostics(self):
        print("Running full system diagnostics...")
        self.check_power()
        self.check_sensors()
        self.check_motors()
        print("Diagnostics complete.")


# Eksempel på brug af RobotDiagnostics
if __name__ == "__main__":
    power_management = PowerManagement(voltage_pin=1, current_pin=2)  # Brug dine eksisterende moduler
    sensors = {
        "ToF": ToFSensor(),
        "IR": IRSensor()
    }
    motors = MotorController()

    diagnostics = RobotDiagnostics(power_management, sensors, motors)
    diagnostics.run_diagnostics()
