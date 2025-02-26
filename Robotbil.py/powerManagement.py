import time


class PowerManagement:
    def __init__(self, voltage_pin, current_pin):
        self.voltage_pin = voltage_pin
        self.current_pin = current_pin

    def read_voltage(self):
        # Simulerer læsning af spænding fra en sensor (udskift med faktisk måling)
        voltage = self.simulate_sensor(self.voltage_pin)
        return voltage

    def read_current(self):
        # Simulerer læsning af strømforbrug (udskift med faktisk måling)
        current = self.simulate_sensor(self.current_pin)
        return current

    def simulate_sensor(self, pin):
        # Simulering af en sensorværdi
        return round(7.4 + 0.1 * (pin % 2), 2)  # Simulerer spændingsfald og strømvariationer

    def monitor_power(self):
        voltage = self.read_voltage()
        current = self.read_current()
        print(f"Voltage: {voltage} V, Current: {current} A")


# Eksempel på at bruge PowerManagement-klassen
if __name__ == "__main__":
    power_manager = PowerManagement(voltage_pin=1, current_pin=2)
    while True:
        power_manager.monitor_power()
        time.sleep(2)  # Opdater hver 2. sekund
