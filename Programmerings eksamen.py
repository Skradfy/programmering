class Password:
    def __init__(self):
        self.list = []
        self.state = "menu"

    def menu(self):
        choice = int(input("""
            _______________________________________________________________________________________
            |                                                                                     |
            |          Skriv dit password efter du har valg det du ønsker at tilføje              |
            |                                                                                     |
            |                                                                                     |
            |           indtast navn og alder (kræver password 1).............tast 1              |
            |           indtast by og postnummer (kræver password2)...........tast 2              |
            |_____________________________________________________________________________________|        

            """))
        # dictionary
        choices = {
            1: "indtast_navn_og_alder",
            2: "by_og_postnummer",
        }
        self.state = choices.get(choice, "menu")

    def indtast_navn_og_alder(self):
        password = input("Type in the first password!")
        if password != "1semester":
            return password
        else:
            navn = input("Indtast dit navn")
            alder = input("indtast din alder")
            print(f"Dit navn er {navn} og du er {alder} år gammel")
            self.list = f"Du hedder {navn} og er {alder} gammel"

            filename = "C:\\Users\\rolle\\Desktop\\Pycharm koder\\FSM\\pass1.txt"
            with open(filename, 'a') as file:
                file.write(str(f"{self.list}\n"))
                file.close()
            print(f"Data saved {self.list} to {filename}")
            self.state = "dato"

    def by_og_postnummer(self):
        password = input("Type in the second password!")
        if password != "2semester":
            return password
        else:
            by = input("Indtast din by")
            postnummer = input("indtast dit postnummer")
            print(f"Din by er {by} og du bor i postnummer: {postnummer}")
            self.list = f"Din by er {by} og du bor i postnummer: {postnummer}"

            filename = "C:\\Users\\rolle\\Desktop\\Pycharm koder\\FSM\\pass2.txt"
            with open(filename, 'a') as file:
                file.write(str(f"{self.list}\n"))
                file.close()
            print(f"Data saved {self.list} to {filename}")
            self.state = "aar_boet_i_byen"

    def dato(self):
        dagsdato = input("Indtast dags dato")
        print(f"Du indtastede: {dagsdato}")

        self.list = dagsdato

        filename = "C:\\Users\\rolle\\Desktop\\Pycharm koder\\FSM\\pass1.txt"
        with open(filename, 'a') as file:
            file.write(str(f"{self.list}\n"))
            file.close()
        print(f"Data saved {self.list} to {filename}")
        self.state = "end"

    def aar_boet_i_byen(self):
        aar_boet_i_byen = input("Hvor mange år har du boet i byen?")
        print(f"Du indtastede: {aar_boet_i_byen}")

        self.list = aar_boet_i_byen

        filename = "C:\\Users\\rolle\\Desktop\\Pycharm koder\\FSM\\pass2.txt"
        with open(filename, 'a') as file:
            file.write(str(f"{self.list}\n"))
            file.close()
        print(f"Data saved {self.list} to {filename}")
        self.state = "end"

    def end(self):
        self.state = "exit"

    def run(self):  # string decorators/state patterns - yderligere metoder: State Patterns, Enumerations,
        # Framework (from transitions import machine )
        while self.state != "exit":
            if self.state == "menu":
                self.menu()
            elif self.state == "indtast_navn_og_alder":
                self.indtast_navn_og_alder()
            elif self.state == "by_og_postnummer":
                self.by_og_postnummer()
            elif self.state == "dato":
                self.dato()
            elif self.state == "aar_boet_i_byen":
                self.aar_boet_i_byen()
            elif self.state == "end":
                self.end()


if __name__ == "__main__":
    manager = Password()
    manager.run()
