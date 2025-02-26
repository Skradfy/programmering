from math import sqrt


class OhmsLov:
    def __init__(self):
        self.state = "menu"
        self.P = 0
        self.R = 0
        self.I = 0
        self.U = 0

    def menu(self):
        choice = (input("""
            _______________________________________________________________________________________
            |                                                                                     |
            |                                Ohms Lov udregner                                    |
            |                                                                                     |
            |     Du ønsker at få P og kender du U og I:........(P=U*I)............tast 1         |
            |     Du ønsker at få P og kender du I og R:........(P=R*I**2).........tast 2         |
            |     Du ønsker at få P og kender du U og R:........(P=U**2/R).........tast 3         |
            |                                                                                     |
            |     Du ønsker at få R og kender du U og I:........(R=U/I)............tast 4         |
            |     Du ønsker at få R og kender du P og I:........(R=P/I**2).........tast 5         |
            |     Du ønsker at få R og kender du U og P:........(R=U**2/P).........tast 6         |
            |                                                                                     |
            |     Du ønsker at få I og kender du U og R:........(I=U/R)...........tast 7          |
            |     Du ønsker at få I og kender du P og R:........(I=sqrt(P/R)......tast 8          |   
            |     Du ønsker at få I og kender du P og U: .......(I=P/U)...........tast 9          |
            |                                                                                     |
            |     Du ønsker at få U og kender du P og I:........(U=P/I)...........tast 10         |
            |     Du ønsker at få U og kender du I og R:........(U=I*R)...........tast 11         |
            |     Du ønsker at få U og kender du P og R:........(U=sqrt(P*R)......tast 12         |
            |                                                                                     |
            |     For at afslutte.............................................tast q              |
            |_____________________________________________________________________________________|        
            """))

        choices = {
            "1": "ap",
            "2": "bp",
            "3": "cp",
            "4": "ar",
            "5": "br",
            "6": "cr",
            "7": "ai",
            "8": "bi",
            "9": "ci",
            "10": "au",
            "11": "bu",
            "12": "cu",
            "q": "end"
        }

        self.state = choices.get(choice, "menu")

    def ap(self):
        uvolt = float(input("Indtast U"))
        istrom = float(input("Indtast I"))
        self.P = uvolt * istrom
        print(f"{uvolt} * {istrom} = {self.P}")
        input("Tryk Enter for at fortsætte...")
        self.state = "menu"

    def bp(self):
        istrom = float(input("Indtast I"))
        rmodstand = float(input("Indtast R"))
        self.P = rmodstand * istrom ** 2
        print(f" {rmodstand} * {istrom}**2 = {self.P}")
        input("Tryk Enter for at fortsætte...")
        self.state = "menu"

    def cp(self):
        uvolt = float(input("Indtast U"))
        rmodstand = float(input("Indtast R"))
        self.P = uvolt ** 2 / rmodstand
        print(f" {uvolt}**2 / {rmodstand} = {self.P}")
        input("Tryk Enter for at fortsætte...")
        self.state = "menu"

    def ar(self):
        uvolt = float(input("Indtast U"))
        istrom = float(input("Indtast I"))
        self.R = uvolt / istrom
        print(f" {uvolt} / {istrom} = {self.R}")
        input("Tryk Enter for at fortsætte...")
        self.state = "menu"

    def br(self):
        pwatt = float(input("Indtast P"))
        istrom = float(input("Indtast I"))
        self.R = pwatt / istrom ** 2
        print(f"{pwatt} / {istrom}**2 = {self.R}")
        input("Tryk Enter for at fortsætte...")
        self.state = "menu"

    def cr(self):
        uvolt = float(input("Indtast U"))
        pwatt = float(input("Indtast P"))
        self.R = uvolt ** 2 / pwatt
        print(f" {uvolt} ** 2 / {pwatt} = {self.R}")
        input("Tryk Enter for at fortsætte...")
        self.state = "menu"

    def ai(self):
        uvolt = float(input("Indtast U"))
        rmodstand = float(input("Indtast R"))
        self.I = uvolt / rmodstand
        print(f" {uvolt} / {rmodstand} = {self.I}")
        input("Tryk Enter for at fortsætte...")
        self.state = "menu"

    def bi(self):
        pwatt = float(input("Indtast P"))
        rmodstand = float(input("Indtast R"))
        self.I = sqrt(pwatt / rmodstand)
        print(f" sqrt({pwatt} / {rmodstand}) = {self.I}")
        input("Tryk Enter for at fortsætte...")
        self.state = "menu"

    def ci(self):
        pwatt = float(input("Indtast P"))
        uvolt = float(input("Indtast U"))
        self.I = pwatt / uvolt
        print(f" {pwatt} / {uvolt} = {self.I}")
        input("Tryk Enter for at fortsætte...")
        self.state = "menu"

    def au(self):
        pwatt = float(input("Indtast P"))
        istrom = float(input("Indtast = I"))
        self.U = pwatt / istrom
        print(f" {pwatt} / {istrom} = {self.U}")
        input("Tryk Enter for at fortsætte...")
        self.state = "menu"

    def bu(self):
        istrom = float(input("Indtast I"))
        rmodstand = float(input("Indtast R"))
        self.U = istrom * rmodstand
        print(f" {istrom} * {rmodstand} = {self.U}")
        input("Tryk Enter for at fortsætte...")
        self.state = "menu"

    def cu(self):
        pwatt = float(input("Indtast P"))
        rmodstand = float(input("Indtast R"))
        self.U = sqrt(pwatt * rmodstand)
        print(f" sqrt({pwatt} * {rmodstand}) = {self.U}")
        input("Tryk Enter for at fortsætte...")
        self.state = "menu"

    def end(self):
        self.state = "exit"

    def run(self):
        while self.state != "exit":
            if self.state == "menu":
                self.menu()
            if self.state == "ap":
                self.ap()
            if self.state == "bp":
                self.bp()
            if self.state == "cp":
                self.cp()
            if self.state == "ar":
                self.ar()
            if self.state == "br":
                self.br()
            if self.state == "cr":
                self.cr()
            if self.state == "ai":
                self.ai()
            if self.state == "bi":
                self.bi()
            if self.state == "ci":
                self.ci()
            if self.state == "au":
                self.au()
            if self.state == "bu":
                self.bu()
            if self.state == "cu":
                self.cu()

            if self.state == "end":
                self.end()


if __name__ == "__main__":
    manager = OhmsLov()
    manager.run()
