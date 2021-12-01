class Complex:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.x}{"" if self.y < 0 else "+"}{self.y}i'

    def __add__(self, other):
        return Complex(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Complex(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Complex(self.x * other.x - self.y * other.y, self.x * other.y + self.y * other.x)


c1 = Complex(2, 3)
c2 = Complex(-1, 1)

print(f'Число 1: {c1}')
print(f'Число 2: {c2}')
print(f'Сложение: {c1 + c2}')
print(f'Вычитание: {c1 - c2}')
print(f'Умножение: {c1 * c2}')
