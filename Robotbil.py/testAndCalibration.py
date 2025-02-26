class TestAndCalibration:
    def __init__(self):
        self.calibration_data = {
            "tof_sensor": None,
            "ir_sensor": None,
            "motors": None
        }

    def calibrate_tof_sensor(self):
        # Simulerer kalibrering af TOF-sensor (udskift med din kalibreringsalgoritme)
        print("Calibrating TOF sensor...")
        self.calibration_data['tof_sensor'] = 0.95  # Simuleret kalibreringsværdi
        print(f"TOF sensor calibration complete: {self.calibration_data['tof_sensor']}")

    def calibrate_ir_sensor(self):
        # Simulerer kalibrering af IR-sensor
        print("Calibrating IR sensor...")
        self.calibration_data['ir_sensor'] = 0.9  # Simuleret kalibreringsværdi
        print(f"IR sensor calibration complete: {self.calibration_data['ir_sensor']}")

    def calibrate_motors(self):
        # Simulerer kalibrering af motorer
        print("Calibrating motors...")
        self.calibration_data['motors'] = 1.0  # Simuleret kalibreringsværdi
        print(f"Motors calibration complete: {self.calibration_data['motors']}")

    def run_tests(self):
        # Simulerer nogle tests, der kan køres efter kalibrering
        print("Running system tests...")
        if all(value is not None for value in self.calibration_data.values()):
            print("All systems are calibrated and ready!")
        else:
            print("Some systems need calibration!")

# Eksempel på at bruge TestAndCalibration-klassen
if __name__ == "__main__":
    test_calibration = TestAndCalibration()
    test_calibration.calibrate_tof_sensor()
    test_calibration.calibrate_ir_sensor()
    test_calibration.calibrate_motors()
    test_calibration.run_tests()
