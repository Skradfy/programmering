from time import sleep


class Lommeregner:
    def __init__(self):
        self.division = None
        self.multiplikation = None
        self.subtraction = None
        self.addition = None
        self.state = "menu"

    def menu(self):
        choice = int(input("""
            _______________________________________________________________________________________
            |                                                                                     |
            |                                Regnemaskine Aps                                     |
            |                                                                                     |
            |                                                                                     |
            |           Vil du addere?........................................tast 1              |
            |           Vil du subtrahere?....................................tast 2              |
            |           Vil du multiplicere?..................................tast 3              |
            |           Vil du dividere?......................................tast 4              |
            |           Quit..................................................tast 5              |
            |                                                                                     |
            |_____________________________________________________________________________________|        

            """))
        choices = {
            1: "addere",
            2: "subtrahere",
            3: "multiplicere",
            4: "dividere",
            5: "exit",
        }

        self.state = choices.get(choice, "menu")

    def addere(self):
        tal1 = float(input("Vælg et tal"))
        tal2 = float(input("Vælg et tal"))
        self.addition = tal1 + tal2
        print(float(round(self.addition, 2)))
        sleep(5)
        self.state = "menu"

    def subtrahere(self):
        tal1 = float(input("Vælg et tal"))
        tal2 = float(input("Vælg et tal"))
        self.subtraction = tal1 - tal2
        print(float(round(self.subtraction, 2)))
        sleep(5)
        self.state = "menu"

    def multiplicere(self):
        tal1 = float(input("Vælg et tal"))
        tal2 = float(input("Vælg et tal"))
        self.multiplikation = tal1 * tal2
        print(float(round(self.multiplikation, 2)))
        sleep(5)
        self.state = "menu"

    def dividere(self):
        tal1 = float(input("Vælg et tal"))
        tal2 = float(input("Vælg et tal"))
        self.division = tal1 / tal2
        print(float(round(self.division, 2)))
        sleep(5)
        self.state = "menu"

    def end(self):
        self.state = "exit"

    def run(self):
        while self.state != "exit":
            if self.state == "menu":
                self.menu()
            if self.state == "addere":
                self.addere()
            if self.state == "subtrahere":
                self.subtrahere()
            if self.state == "multiplicere":
                self.multiplicere()
            if self.state == "dividere":
                self.dividere()
            if self.state == "end":
                self.end()


if __name__ == "__main__":
    manager = Lommeregner()
    manager.run()
