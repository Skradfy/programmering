class SensorFusion:
    def __init__(self, tof_sensor, ir_sensor):
        self.tof_sensor = tof_sensor
        self.ir_sensor = ir_sensor

    def get_fused_data(self):
        tof_distance = self.tof_sensor.get_distance()
        ir_reflection = self.ir_sensor.get_reflection()

        # Simpel sensorfusion logik: Justér målinger fra ToF og IR for at få en samlet vurdering
        if ir_reflection < 0.5:  # Eksempelgrænse
            adjusted_distance = tof_distance * 1.1  # Justerer ToF-afstanden
        else:
            adjusted_distance = tof_distance

        return adjusted_distance


# Simulerede sensor klasser
class ToFSensor:
    def get_distance(self):
        return 20.0  # Eksempelværdi


class IRSensor:
    def get_reflection(self):
        return 0.3  # Eksempelværdi


# Eksempel på brug af SensorFusion
if __name__ == "__main__":
    tof_sensor = ToFSensor()
    ir_sensor = IRSensor()

    fusion = SensorFusion(tof_sensor, ir_sensor)
    fused_data = fusion.get_fused_data()
    print(f"Fused sensor data: {fused_data} cm")
