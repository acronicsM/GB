# Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

CNT_NUM = 5
CNT_COL = 4
ar = [[0 for _ in range(CNT_COL)] for _ in range(CNT_NUM)]

for key_x, x in enumerate(ar[:CNT_NUM - 1]):
    sum_str = 0
    for key_y, y in enumerate(x[: CNT_COL - 1]):
        value = int(input(f'Ввечиде значение {key_x + 1} строки {key_y + 1} колонки: '))
        sum_str += value
        ar[CNT_NUM - 1][key_y] += value
        x[key_y] = value

    x[CNT_COL - 1] = sum_str
    ar[CNT_NUM - 1][CNT_COL - 1] += sum_str

for i in ar:
    print(i)
