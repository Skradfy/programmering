import time
from threading import Thread


class TempMonitorControl:
    def __init__(self):
        self.state = "menu"
        self.temperature = 37
        self.running = True

    def menu(self):
        choice = int(input("""
            _______________________________________________________________________________________
            |                                                                                     |
            |                                State opgave onsdag 1                                |
            |                                                                                     |
            |                                                                                     |
            |           Give cooling.........................................press 1              |
            |           Give heat............................................press 2              |
            |           Stay neutral.........................................press 3              |
            |           Stop machine.........................................press 4              |
            |                                                                                     |
            |_____________________________________________________________________________________|        

            """))
        choices = {
            1: "give_cooling",
            2: "give_heat",
            3: "stay_neutral",
            4: "end",
        }
        self.state = choices.get(choice, "menu")

    def give_cooling(self):
        cooling_amount = int(input("Enter cooling amount: "))
        self.temperature -= cooling_amount
        print(f"Cooling applied. New temperature: {self.temperature}°C")
        self.check_critical_low()
        self.state = "menu"

    def give_heat(self):
        heat_amount = int(input("Enter heat amount: "))
        self.temperature += heat_amount
        print(f"Heat applied. New temperature: {self.temperature}°C")
        self.state = "menu"

    def stay_neutral(self):
        print("Staying neutral. Current temperature: {self.temperature}°C")
        self.state = "menu"

    def check_critical_low(self):
        if self.temperature <= 20:
            print(f"Warning: Critical low temperature reached: {self.temperature}°C")

    def end(self):
        self.state = "exit"
        self.running = False
        print("Stopping the machine.")

    def automatic_temperature_drop(self):
        while self.running:
            time.sleep(5)
            if self.running:
                self.temperature -= 1
                print(f"Automatic temperature drop. New temperature: {self.temperature}°C")
                self.check_critical_low()

    def run(self):
        temp_drop_thread = Thread(target=self.automatic_temperature_drop)
        temp_drop_thread.start()

        while self.state != "exit":
            if self.state == "menu":
                self.menu()
            elif self.state == "give_cooling":
                self.give_cooling()
            elif self.state == "give_heat":
                self.give_heat()
            elif self.state == "stay_neutral":
                self.stay_neutral()
            elif self.state == "end":
                self.end()

        temp_drop_thread.join()  # Ensure the thread has finished


if __name__ == "__main__":
    manager = TempMonitorControl()
    manager.run()
