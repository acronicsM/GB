class MyDivisionZero(Exception):
    def __init__(self, divisible, divisor):
        self.divisible = divisible
        self.divisor = divisor

    def __str__(self):
        return f'Ошибка деления на ноль! Выражение: {self.divisible}/{self.divisor}'


def delenie(a, b):
    try:
        c= a/b
    except ZeroDivisionError:
        raise MyDivisionZero(a, b)

    return c


d1 = delenie(3, 1)
d2 = delenie(0, 1)

try:
    d3 = delenie(3, 0)
except MyDivisionZero as mdz:
    print(mdz)