# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

def sum_digit(num):
    summ = 0
    while num != 0:
        summ += num % 10
        num //= 10

    return summ


num = -1
summ = 0
isk = 0

while num != 0:
    num = int(input(f'Введите натуральное число, для завершения последовательности введите 0: '))
    res = sum_digit(num)

    if res > summ:
        summ = res
        isk = num

print(f'Наибольшая сумма ({summ}) у числа {isk}')
