from abc import ABC, abstractmethod


class Clothes(ABC):
    calculation_Coat = 0
    calculation_Suit = 0

    def __init__(self, name, cloth_require):
        self.name = name
        self.require = cloth_require

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def add_to_reserve(self):
        pass

    @property
    def cloth_require(self):
        return self.require


class Coat(Clothes):
    def __init__(self, size):
        super().__init__('Coat', size / 6.5 + 0.5)

    def add_to_reserve(self):
        Clothes.calculation_Coat += self.require

    @property
    def get_all(self):
        return Clothes.calculation_Coat


class Suit(Clothes):
    def __init__(self, size):
        super().__init__('Suit', 2 / size + 0.3)

    def add_to_reserve(self):
        Clothes.calculation_Suit += self.require

    @property
    def get_all(self):
        return Clothes.calculation_Suit


c1 = Coat(11)
c2 = Coat(121)
c3 = Coat(4)

s1 = Suit(45)
s2 = Suit(455)
s3 = Suit(4)

c1.add_to_reserve()
c2.add_to_reserve()
c3.add_to_reserve()

s1.add_to_reserve()
s2.add_to_reserve()
s3.add_to_reserve()

print(f'c1 - {c1.cloth_require}')
print(f'c2 - {c2.cloth_require}')
print(f'c3 - {c3.cloth_require}')

print(f's1 - {s1.cloth_require}')
print(f's2 - {s2.cloth_require}')
print(f's3 - {s3.cloth_require}')

print(f'Всего требуется на пальто {c1.get_all}')
print(f'Всего требуется на костюм {s1.get_all}')
