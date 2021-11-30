class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = {"wage": wage, "bonus": bonus}

    def get_income(self):
        return self.__income


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        income = self.get_income()
        return income['wage'] + income['bonus']


w1 = Position('Ivan', 'Ivanov', 'pos1', 100, 10)
print(w1.get_full_name())
print(w1.get_total_income())
