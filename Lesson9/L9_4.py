class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Машина поехала')

    def stop(self):
        print(f'Машина остановилась')

    def turn(self, direction):
        print(f'Машина повернула в {direction}')

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self.speed > 60:
            print(f'{self.speed} Превышение скорости!')
        else:
            super().show_speed()


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self.speed > 40:
            print(f'{self.speed} Превышение скорости!')
        else:
            super().show_speed()


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


tc = TownCar(20, 'красный', '№1')
sc = SportCar(40, 'белый', '№2')
wc = WorkCar(60, 'синий', '№3')
pc = PoliceCar(100, 'черный', '№3')

print(f'TownCar скорость: ')
tc.show_speed()

print(f'SportCar скорость: ')
sc.show_speed()

print(f'WorkCar скорость: ')
wc.show_speed()
wc.speed = 30
print(f'WorkCar скорость: ')
wc.show_speed()

print(f'PoliceCar скорость: ')
pc.show_speed()
