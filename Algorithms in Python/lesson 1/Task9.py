# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
print('Введите 3 целых цисла')
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))

if a > b:
    if b > c:
        print(f'Среднее число: {b}')
    elif a > c:
        print(f'Среднее число: {c}')
    else:
        print(f'Среднее число: {a}')
elif a > c:
    print(f'Среднее число: {a}')
else:
    print(f'Среднее число: {b}')