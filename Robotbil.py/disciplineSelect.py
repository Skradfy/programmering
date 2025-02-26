class DisciplineSelect:
    def __init__(self):
        self.disciplines = {
            1: "Wall Follow",
            2: "SUMO Battle",
            3: "Line Follow",
            4: "Remote Control"
        }

    def display_disciplines(self):
        print("Available Disciplines:")
        for key, value in self.disciplines.items():
            print(f"{key}: {value}")

    def select_discipline(self, choice):
        if choice in self.disciplines:
            print(f"Discipline selected: {self.disciplines[choice]}")
            return self.disciplines[choice]
        else:
            print("Invalid choice. Please select a valid discipline.")
            return None

# Eksempel på brug af DisciplineSelect-klassen
if __name__ == "__main__":
    selector = DisciplineSelect()
    selector.display_disciplines()
    user_choice = int(input("Select a discipline by number: "))
    selector.select_discipline(user_choice)
