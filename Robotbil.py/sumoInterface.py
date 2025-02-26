class SumoInterface:
    def __init__(self, sumo_logic):
        self.sumo_logic = sumo_logic

    def start_sumo(self):
        print("Starting SUMO Battle...")
        self.sumo_logic.start()

    def stop_sumo(self):
        print("Stopping SUMO Battle...")
        self.sumo_logic.stop()

    def get_current_status(self):
        status = self.sumo_logic.get_status()
        print(f"SUMO status: {status}")

# Simulering af SUMO-logik
class SumoLogic:
    def start(self):
        print("SUMO battle initiated.")

    def stop(self):
        print("SUMO battle stopped.")

    def get_status(self):
        # Simulerer SUMO-status
        return "In Progress"  # Eksempelstatus

# Eksempel på brug af SumoInterface-klassen
if __name__ == "__main__":
    logic = SumoLogic()
    interface = SumoInterface(logic)

    interface.start_sumo()
    interface.get_current_status()
    interface.stop_sumo()
