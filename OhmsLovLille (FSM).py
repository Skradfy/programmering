import os.path


class OhmsLovLille:
    def __init__(self):
        self.list = []
        self.state = "menu"
        self.R = 0
        self.I = 0
        self.U = 0

    def menu(self):
        choice = (input("""
            _______________________________________________________________________________________
            |                                                                                     |
            |                                Ohms Lov udregner                                    |
            |                                                                                     |
            |     Du ønsker at få U (spænding) (U = I * R)...............tast 1                   |
            |     Du ønsker at få I (strøm) (I = U / R)..................tast 2                   |
            |     Du ønsker at få R (modstand) (R = U / I)...............tast 3                   |
            |                                                                                     |
            |                                                                                     |
            |     For at afslutte.............................................tast q              |
            |_____________________________________________________________________________________|        
            """))

        choices = {
            "1": "ustate",
            "2": "istate",
            "3": "rstate",
            "q": "end"
        }

        self.state = choices.get(choice, "menu")

    def ustate(self):
        istrom = float(input("Indtast I - strømmen"))
        rmodstand = float(input("Indtast R - modstanden"))
        self.U = round(istrom * rmodstand, 4)
        print(f"Spændingen er {self.U} Volt")

        filename = "C:\\Users\\rolle\\Desktop\\Pycharm koder\\FSM\\ohm.txt"
        if os.path.isfile(filename):
            with open(filename, 'a') as file:
                self.list = [self.U]
                file.write(str(f"{self.list}\n"))
                file.close()
                print(filename)
                self.state = "menu"

        else:
            with open(filename, 'w') as file:
                self.list = [self.U]
                file.write(str(f"{self.list}\n"))
                file.close()
                print(filename)
                self.state = "menu"

    def istate(self):
        uvolt = float(input("Indtast U - spændingen"))
        rmodstand = float(input("Indtast R - modstanden"))
        self.I = round(uvolt / rmodstand, 4)
        print(f"Strømmen er {self.I} Ampere")

        filename = "C:\\Users\\rolle\\Desktop\\Pycharm koder\\FSM\\ohm.txt"
        if os.path.isfile(filename):
            with open(filename, 'a') as file:
                self.list = [self.I]
                file.write(str(f"{self.list}\n"))
                file.close()
                print(filename)
                self.state = "menu"

        else:
            with open(filename, 'w') as file:
                self.list = [self.I]
                file.write(str(f"{self.list}\n"))
                file.close()
                print(filename)
                self.state = "menu"

    def rstate(self):
        uvolt = float(input("Indtast U - spændingen"))
        istrom = float(input("Indtast I - strømmen"))
        self.R = round(uvolt / istrom, 4)
        print(f"modstanden er {self.R} Ohm")

        filename = "C:\\Users\\rolle\\Desktop\\Pycharm koder\\FSM\\ohm.txt"
        if os.path.isfile(filename):
            with open(filename, 'a') as file:
                self.list = [self.R]
                file.write(str(f"{self.list}\n"))
                file.close()
                print(filename)
                self.state = "menu"

        else:
            with open(filename, 'w') as file:
                self.list = [self.U]
                file.write(str(f"{self.list}\n"))
                file.close()
                print(filename)
                self.state = "menu"

    def end(self):
        self.state = "exit"

    def run(self):
        while self.state != "exit":
            if self.state == "menu":
                self.menu()
            if self.state == "ustate":
                self.ustate()
            if self.state == "istate":
                self.istate()
            if self.state == "rstate":
                self.rstate()
            if self.state == "end":
                self.end()


if __name__ == "__main__":
    manager = OhmsLovLille()
    manager.run()
