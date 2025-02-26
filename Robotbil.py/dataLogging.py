import csv
import time

class DataLogger:
    def __init__(self, log_file="robot_data_log.csv"):
        self.log_file = log_file
        self.fieldnames = ['timestamp', 'sensor', 'value']

        # Opret en ny fil og skriv header
        with open(self.log_file, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.fieldnames)
            writer.writeheader()

    def log(self, sensor_name, value):
        with open(self.log_file, mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.fieldnames)
            writer.writerow({'timestamp': time.time(), 'sensor': sensor_name, 'value': value})
        print(f"Logged {sensor_name}: {value}")

# Eksempel på brug af DataLogger
if __name__ == "__main__":
    logger = DataLogger()

    # Simulering af sensordata logning
    logger.log('ToF Sensor', 15.2)
    logger.log('IR Sensor', 0.9)
