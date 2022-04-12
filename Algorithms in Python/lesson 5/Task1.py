# Пользователь вводит данные о количестве предприятий,
# их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования предприятий,
# чья прибыль выше среднего и ниже среднего.

from collections import defaultdict

QUARTER = 4
all = defaultdict(int)
all_sum = 0
above = ''
below = ''
divide = '-'*20

quantity = int(input('Введите количество предприятий (отличное от 0): '))

for _ in range(quantity):
    name = input('Введите название предприятия: ')

    for i in range(QUARTER):
        all[name] += int(input(f'Введите прибыль {i + 1} квартала: '))

    all[name] /= 4
    all_sum += all[name]

average = all_sum / quantity

for key, value in all.items():
    if value >= average:
        above += f'{key}\n'
    else:
        below += f'{key}\n'

print(f'Выше среднего\n{above.rstrip()}\n{divide}\nНиже среднего\n{below.rstrip()}')



