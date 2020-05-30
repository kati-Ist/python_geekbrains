class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        print(f"Worker: {self.name} {self.surname} works as a {self.position}")

    def get_total_income(self):
        print(f"Salary: {sum(self._income.values())}")


a = Position("Bob", "Bobson", "Programmer", 777777, 333333)
a.get_full_name()
a.get_total_income()
