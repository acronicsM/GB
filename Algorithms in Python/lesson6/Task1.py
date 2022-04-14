# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.


# Задача для анализа  из  ДЗ lesson2 - Task3:
# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.

import sys
from collections import deque


def decor_func(func):
    def decor(*args, **kwargs):
        value, variables = func(*args, **kwargs)

        print(f'Использование памяти функцией: {func.__name__}')
        sum_size = 0
        for n, v in variables.items():
            size = sys.getsizeof(v)
            print(f'{n}: {size}')
            sum_size += size
        print(f'Суммарное значение: {sum_size}')
        return value
    return decor


@decor_func
def expand_num(num_):
    """Развернуть через число"""
    num_int = num_
    num2 = 0

    while num_int > 0:
        num2 = num2*10 + num_int % 10
        num_int = num_int // 10

    return num2, locals()


@decor_func
def expand_str(num_):
    """Развернуть через строку"""
    num_str = str(num_)[::-1]

    return num_str, locals()


@decor_func
def expand_deque(num_):
    """Развернуть через очередь"""
    num_deque = deque(str(num_))
    num_deque.reverse()

    return num_deque, locals()


# num = int(input('введите натурильное число: '))
num = 8956895239057673458345725496734582394057238748934534578934573489563489563457863478563457865746745634785634

print(num)
print(f'Версия OS: {sys.platform}\nВерсия pytnon: {sys.version}')

expand_num(num)
expand_str(num)
expand_deque(num)


# Использование памяти функцией: expand_num
# num_: 76
# num_int: 24
# num2: 76
# Суммарное значение: 176
# Использование памяти функцией: expand_str
# num_: 76
# num_str: 161
# Суммарное значение: 237
# Использование памяти функцией: expand_deque
# num_: 76
# num_deque: 1152
# Суммарное значение: 1228


#Вывод:
# 1) Наилучшие результаты по памяти занимает функция переворачивающия число как число,
# так как для хранения используется переменная типа int для хранения 28 байта для числа до 9 цифр
# с увеличение  на 4 байта каждые через каждые 10 цифр
# 2) Переворачивания числа в виде строки будет занимать больший размер так как пустая строка занимает 49 байт
# и увеличивается на 1 байт за каждый символ
# 3) Худший показатель у очереди deque так как уже пустая очередь занимает 624 байта
# c увеличение каждые 64 элемента на 528 байт
