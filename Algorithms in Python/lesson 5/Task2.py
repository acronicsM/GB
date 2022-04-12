# Написать программу сложения и умножения двух положительных целых шестнадцатеричных чисел.
# При этом каждое число представляется как коллекция, элементы которой — цифры числа.
# Например, пользователь ввёл A2 и C4F.
# Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque

BASIS_DEC = 10
BASIS_HEX = 16

alphabet_16 = deque([str(i) for i in range(BASIS_DEC)] + ['A', 'B', 'C', 'D', 'E', 'F'])  # шестнадцатеричный алфавит
alphabet_10 = deque([i for i in range(BASIS_HEX)])  # десятичный алфавит до 16
alphabet_HEX = dict(zip(alphabet_16, alphabet_10))
alphabet_XEH = dict(zip(alphabet_10, alphabet_16))


def summ_hex(d1_, d2_):
    global alphabet_HEX, alphabet_XEH, BASIS_HEX

    summand1, summand2 = d1_.copy(), d2_.copy()
    d_summ = deque()  # Итоговая сумма
    overflow_summ = 0  # переходящий десяток

    for i in range(len(summand1)):
        elem1, elem2 = summand1.pop(), summand2.pop()  # Достаем по 1 элементу с конца чисел

        s1 = alphabet_HEX[elem1] + alphabet_HEX[elem2] + overflow_summ

        if s1 >= BASIS_HEX:
            n = alphabet_XEH[s1 - BASIS_HEX]
            overflow_summ = 1
        else:
            n = alphabet_XEH[s1]
            overflow_summ = 0

        d_summ.appendleft(n)

    if overflow_summ != 0:  # Добавляем последний переходящий десяток если он есть
        d_summ.appendleft(overflow_summ)

    return d_summ


def multi_hex(d1_, d2_):
    global alphabet_HEX, alphabet_XEH, BASIS_HEX

    multiplier1, multiplier2 = d1_.copy(), d2_.copy()
    overflow_multi = 0
    d_summ = False

    for x in range(len(multiplier1)):
        elem1 = multiplier1.pop()
        elem2 = multiplier2.copy()
        elem2.reverse()  # Разворачиваем для удобства умножения

        # Добавляем нули в зависимости от итерации что бы при сложении длины чисел были одинаковые
        d_multi_2 = deque('0'*x)

        for i in elem2:
            m = alphabet_HEX[elem1] * alphabet_HEX[i] + overflow_multi
            if m > BASIS_HEX:
                n = alphabet_XEH[m % BASIS_HEX]
                overflow_multi = m // BASIS_HEX
            else:
                overflow_multi = 0
                n = alphabet_XEH[m]

            d_multi_2.appendleft(n)

        if overflow_multi > 0:
            d_multi_2.appendleft(alphabet_XEH[overflow_multi])
            overflow_multi = 0

        if not d_summ:
            d_summ = d_multi_2
        else:
            d_summ.appendleft('0')  # Добавляем ноль что бы при сложении длины чисел были одинаковые
            d_summ = summ_hex(d_multi_2, d_summ)  # Сложение

    if overflow_multi > 0:  # Добавляем последний переходящий десяток если он есть
        d_summ.append(alphabet_XEH[overflow_multi])

    return d_summ


def deque_num(str_number1, str_number2):
    max_len = max(len(str_number1), len(str_number2))
    zero = '0' * max_len
    zero_num1 = zero + str_number1
    zero_num2 = zero + str_number2
    number1 = deque(zero_num1[-max_len:])
    number2 = deque(zero_num2[-max_len:])

    return number1, number2


num_1 = input('Введите первое число: ').upper()
num_2 = input('Введите второе число: ').upper()

d1, d2 = deque_num(num_1, num_2)

print(f'{d1} + {d2} = {summ_hex(d1, d2)}')
print(f'{d1} * {d2} = {multi_hex(d1, d2)}')
