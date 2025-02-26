
class Template:
    def __init__(self):
        self.state = "random_word"
        self.tal_100 =[]
    def menu(self):
        choice = int(input("""
            _______________________________________________________________________________________
            |                                                                                     |
            |                                State opgave onsdag 1                                |
            |                                                                                     |
            |                                                                                     |
            |           Generate 10 tal mellem 0 og 100.......................tast 1              |
            |           Udskriv tal mellem 50 og 100..........................tast 2              |
            |           Se nuværende liste....................................tast 3              |
            |           Læg min og max sammen og tilføj liste tal_100.........tast 4              |
            |           Skriv listens indhold til fil list100.txt.............tast 5              |
            |           For at afslutte.......................................tast 6              |
            |_____________________________________________________________________________________|        

            """))

    def random_word(self):
        file1 = open("random_word_hangman.txt", "r")
        print("Output of Readlines after appending")
        print(file1.readlines())
        pass



        self.state = "the_1_state"


    def the_0_state(self):
        int(input("""
             -----
             |   |
                 |
                 |
                 |
                 |
            ---------
            """))

        self.state = "the_1_state"



    def the_1_state(self):
        input("""
             -----
             |   |
             O   |
                 |
                 |
                 |
            ---------
            """)
        self.state = "c"

    def the_2_state(self):

        input("""
             -----
             |   |
             O   |
             |   |
                 |
                 |
            ---------
            """)
        self.state = "the_3_state"

    def the_3_state(self):
        int(input("""
             -----
             |   |
             O   |
            /|   |
                 |
                 |
            ---------
            """))
        self.state = "e"

    def e(self):
        input("vælg her:")
        self.state = "f"

    def f(self):
        input("Vælg her:")
        self.state = "end"

    def end(self):
        self.state = "exit"

    def run(self):
        while self.state != "exit":
            if self.state == "random_word":
                self.random_word()
            if self.state == "a":
                self.a()
            if self.state == "b":
                self.b()
            if self.state == "c":
                self.c()
            if self.state == "d":
                self.d()
            if self.state == "e":
                self.e()
            if self.state == "f":
                self.f()
            if self.state == "end":
                self.end()


if __name__ == "__main__":
    manager = Template()
    manager.run()
