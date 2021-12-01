class DateInitError(Exception):
    pass


class Data:
    def __init__(self, str_data):
        lst_data = Data.parsing(str_data)

        err_data = Data.validus_data(lst_data[0], lst_data[1], lst_data[2])
        if err_data:
            raise DateInitError(err_data)

        self.day = lst_data[0]
        self.month = lst_data[1]
        self.year = lst_data[2]

    @classmethod
    def parsing(cls, str_data):
        lst = str_data.split('-')
        ln = len(lst)
        return int(lst[0]) if lst[0].isdigit() else 0, \
            int(lst[1]) if ln > 1 and lst[1].isdigit() else 0, \
            int(lst[2]) if ln > 2 and lst[2].isdigit() else 0

    @staticmethod
    def validus_data(day, month, year):
        leap = (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)
        num_days = (31, 29 if leap else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
        if year < 1:
            return 'Неверный год'
        elif month < 1 or month > 12:
            return 'Неверный месяц'
        elif day < 1 or day > num_days[month - 1]:
            return 'Неверный день'

        return ''

    def __str__(self):
        return f'{self.year}.{self.month}.{self.day}'


d1_text = '31-12-2021'
try:
    print(Data(d1_text))
except DateInitError as ve:
    print(f'Дата {d1_text}, результат: {ve}')

d2_text = '32-12-2022'
try:
    print(Data(d2_text))
except DateInitError as ve:
    print(f'Дата {d2_text}, результат: {ve}')

d3_text = '12-12--2022'
try:
    print(Data(d3_text))
except DateInitError as ve:
    print(f'Дата {d3_text}, результат: {ve}')
