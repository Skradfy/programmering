from random import randint


class RandomTal:
    list = []
    numbers = []
    list_1 = []
    list_2 = []

    def __init__(self):
        self.numbers = None
        self.state = "menu"

    def menu(self):
        choice = int(input("""
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
▬▬▬▬▬▬▬▬▬ (¯`·._.··¸.-~*´¨¯¨`*·~-.,-(Random Number Generator 3000)-,.-~*´¨¯¨`*·~-.¸··._.·´¯) ▬▬▬▬▬▬▬▬▬▬▬▬
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ Generate 10 numbers from 0-10....................1 ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ Sort the numbers and display them.................2 ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ display...........................................3 ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ End..............................................4 ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ 
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
"""))
        if choice == 1:
            self.state = "generate_numbers"
        elif choice == 2:
            self.state = "sort_numbers_on_two_lists"
        elif choice == 3:
            self.state = "display"
        elif choice == 4:
            self.state = "end"
        else:
            print("Invalid choice, make a new")
            self.state = "menu"

    def generate_numbers(self):
        self.numbers = [randint(1, 10) for _ in range(10)]
        self.list.append(self.numbers)
        print(self.numbers)
        self.state = "menu"

    def sort_numbers_on_two_lists(self):
        self.list_1 = [num for num in self.numbers if num <= 4]
        self.list_2 = [num for num in self.numbers if num >= 5]
        print("List 1 (0-4):", sorted(self.list_1))
        print("List 2 (5-10):", sorted(self.list_2))
        self.state = "menu"

    def display(self):
        print(self.list_1)
        print(self.list_2)
        self.state = "menu"

    def end(self):
        self.state = "exit"

    def run(self):
        while self.state != "exit":
            if self.state == "menu":
                self.menu()
            elif self.state == "generate_numbers":
                self.generate_numbers()
            elif self.state == "sort_numbers_on_two_lists":
                self.sort_numbers_on_two_lists()
            elif self.state == "display":
                self.display()

            if self.state == "end":
                self.end()


if __name__ == "__main__":
    manager = RandomTal()
    manager.run()
