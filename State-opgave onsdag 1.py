from random import randint


class Template:
    def __init__(self):
        self.state = "gen_10_tal"
        self.alle_tal = []
        self.tal_100 = []
        self.added = []

    def gen_10_tal(self):
        self.alle_tal = [randint(0, 100) for _ in range(10)]
        print(f"Her er de 10 tal: {self.alle_tal}")

        for tal in self.alle_tal:
            if 50 < tal < 100:
                self.tal_100.append(tal)
            self.state = "skriv_tal_50_100"

    def skriv_tal_50_100(self):
        print(f"Her er tallene mellem 50 og 100 {self.tal_100}")
        self.state = "max_plus_min_onlist"

    def max_plus_min_onlist(self):
        self.added = (max(self.tal_100)) + (min(self.tal_100))
        print(f"maximum tallet er {(max(self.tal_100))} og minimum tallet er {(min(self.tal_100))} sammen giver det "
              f"{self.added}")
        self.state = "skriv_til_list100"

    def skriv_til_list100(self):
        f = open("list100.txt", "w")
        f.write(str(self.added))
        f.close()
        self.state = "se_nuvarende_liste"

    def se_nuvarende_liste(self):
        f = open("list100.txt", "r")
        print(f.read())
        self.state = "end"

    def end(self):
        self.state = "exit"

    def run(self):
        while self.state != "exit":
            if self.state == "gen_10_tal":
                self.gen_10_tal()
            if self.state == "skriv_tal_50_100":
                self.skriv_tal_50_100()
            if self.state == "max_plus_min_onlist":
                self.max_plus_min_onlist()
            if self.state == "skriv_til_list100":
                self.skriv_til_list100()
            if self.state == "se_nuvarende_liste":
                self.se_nuvarende_liste()
            if self.state == "end":
                self.end()


if __name__ == "__main__":
    manager = Template()
    manager.run()
