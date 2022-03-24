# Найти максимальный элемент среди минимальных элементов столбцов матрицы.

from random import randint as rint

SIZE_A = 5
SIZE_B = 3
MIN_ITEM = 1
MAX_ITEM = 9
matrix = [[rint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_A)] for _ in range(SIZE_B)]
print(*matrix, sep='\n')

lst = []

for x in matrix:
    for key, y in enumerate(x):
        if len(lst) < key + 1:
            lst.append(y)
        elif lst[key] > y:
            lst[key] = y

print(f'\n{lst}')

max_ = lst[0]
for i in lst[1:]:
    if i > max_:
        max_ = i

print(max_)
