import os.path


class ParallelleModstande:

    def __init__(self):
        self.r1 = 0
        self.r2 = 0
        self.r3 = 0
        self.r4 = 0
        self.rmodstand = 0
        self.uvolt = 0
        self.istrom = 0
        self.list = []
        self.state = "parallelle"

    def parallelle(self):
        self.r1 = int(input("Indtast værdien for R1"))
        print(f"Du har valgt værdien {self.r1} for R1")
        self.r4 = int(input("Indtast værdien for R4"))
        print(f"Du har valgt værdien {self.r4} for R4")
        self.uvolt = int(input("Indtast værdien for V"))
        print(f"Du har valgt værdien {self.uvolt} for V")
        self.state = "serie"

    def serie(self):
        choice = int(input("""
            _______________________________________________________________________________________
            |                                                                                     |
            |                               Menu                                                  | 
            |                                                                                     |
            |           Tilføj en modstand mere i serie.......................tast 1              |
            |           beregn strømmen.......................................tast 2              |
            |                                                                                     |
            |_____________________________________________________________________________________|        

            """))
        if choice == 1:
            self.state = "tilfojmodstand"
        elif choice == 2:
            self.state = "beregnstrommen"

        else:
            print("Tastefejl, prøv igen")
            self.state = "serie"

    def tilfojmodstand(self):
        if self.r2 == 0:
            self.r2 = int(input("Hvor mange ohm er R2 på?"))
        elif self.r2 > 0:
            self.r3 = int(input("Hvor mange ohm er R3 på?"))
        else:
            print("Dette kredsløb tillader ikke flere modstande")
        self.state = "serie"

    def beregnstrommen(self):
        if self.r2 == 0:
            self.rmodstand = 1 / ((1 / self.r1) + (1 / self.r4))
            self.istrom = round(self.uvolt / self.rmodstand, 4)
            print(f"Spændingen i kredsløbet er {self.uvolt} Volt \nStrømmen i kredsløbet er: {self.istrom} Ampere \n"
                  f"Modstanden i kredsløbet er {self.rmodstand} Ohm")
        elif self.r2 > 0 and self.r3 == 0:
            self.rmodstand = round(self.r2 + (1 / ((1 / self.r1) + (1 / self.r4)), 4))
            self.istrom = self.uvolt / self.rmodstand
            print(f"Spændingen i kredsløbet er {self.uvolt} Volt\nStrømmen i kredsløbet er: {self.istrom} Ampere \n"
                  f"Modstanden i kredsløbet er {self.rmodstand} Ohm")
        elif self.r2 > 0 and self.r3 > 0:
            self.rmodstand = self.r3 + self.r2 + (1 / ((1 / self.r1) + (1 / self.r4)))
            self.istrom = self.uvolt / self.rmodstand
            print(f"Spændingen i kredsløbet er {self.uvolt} Volt\nStrømmen i kredsløbet er: {self.istrom} Ampere \n"
                  f"Modstanden i kredsløbet er {self.rmodstand} Ohm")
        else:
            print("fejl 40!")
        self.state = "savefile"

    def savefile(self):
        filename = "C:\\Users\\rolle\\Desktop\\Pycharm koder\\FSM\\modst.txt"
        if os.path.isfile(filename):
            with open(filename, 'a') as file:
                self.list = [self.rmodstand, self.istrom, self.uvolt]
                file.write(str(f"{self.list}\n"))
                file.close()
                print(filename)
                self.state = "end"

        else:
            with open(filename, 'w') as file:
                self.list = [self.rmodstand, self.istrom, self.uvolt]
                file.write(str(f"{self.list}\n"))
                file.close()
                print(filename)
                self.state = "end"

    def end(self):
        self.state = "exit"

    def run(self):
        while self.state != "exit":
            if self.state == "parallelle":
                self.parallelle()
            if self.state == "serie":
                self.serie()
            if self.state == "tilfojmodstand":
                self.tilfojmodstand()
            if self.state == "beregnstrommen":
                self.beregnstrommen()
            if self.state == "savefile":
                self.savefile()
            if self.state == "end":
                self.end()


if __name__ == "__main__":
    manager = ParallelleModstande()
    manager.run()
