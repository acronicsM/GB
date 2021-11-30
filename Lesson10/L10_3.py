class Cell:
    def __init__(self, cellule):
        self.cellule = cellule

    def __add__(self, other):
        if not isinstance(other, Cell):
            raise ValueError('Слагаемое не является клеткой')
        else:
            return Cell(self.cellule + other.cellule)

    def __sub__(self, other):
        if not isinstance(other, Cell):
            raise ValueError('Вычитаемое не является клеткой')
        elif other.cellule >= self.cellule:
            raise ValueError('Разность клеток меньше 0')
        else:
            return Cell(self.cellule - other.cellule)

    def __mul__(self, other):
        if not isinstance(other, Cell):
            raise ValueError('Множитель не является клеткой')
        else:
            return Cell(self.cellule * other.cellule)

    def __floordiv__(self, other):
        if not isinstance(other, Cell):
            raise ValueError('Делитель не является клеткой')
        else:
            return Cell(self.cellule // other.cellule)

    def make_order(self, quantity):
        b = '*'
        result = (b*quantity + '\n') * (self.cellule // quantity) + (b * (self.cellule % quantity))
        return result if self.cellule % quantity else result[:-1]


c1 = Cell(4)
c2 = Cell(8)
c3 = Cell(41)
c4 = Cell(12)
c5 = Cell(90)
c6 = Cell(400)
c7 = Cell(1)

print('4 + 8 = ')
try:
    print((c1 + 8).make_order(2))
except ValueError as ve:
    print(f'{ve} \n')


print('4 + 8 = ')
print(f'{(c1+c2).make_order(2)} \n')


print('8 - 41 = ')
try:
    print((c2 - c3).make_order(2))
except ValueError as ve:
    print(f'{ve} \n')

print('41 - 12 = ')
print(f'{(c3+c4).make_order(10)} \n')

print('12 * 1 = ')
print(f'{(c4*c7).make_order(10)} \n')

print('400 // 90 = ')
print(f'{(c6//c5).make_order(10)} \n')
