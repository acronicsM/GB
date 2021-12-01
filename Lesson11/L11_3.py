class NumbersOnly(Exception):

    def __init__(self, line):
        self.line = line

    def __str__(self):
        return f'Строка {self.line} не является числом'


def to_do_digit(str_digit):
    if str_digit.isdigit():
        return int(str_digit)
    else:
        raise NumbersOnly(str_digit)


digit = ''
lst = list()

while digit.lower() != 'stop':

    digit = input('Введите число: ')

    try:
        lst.append(to_do_digit(digit))
    except NumbersOnly as nod:
        print(nod)

print(lst)
