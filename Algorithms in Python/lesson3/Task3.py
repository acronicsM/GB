# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

from random import randint as rint

SIZE = 10
MIN_ITEM = 2
MAX_ITEM = 99
array = [rint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

min_index = max_index = 0
min_ = max_ = array[min_index]

for key, i in enumerate(array[1:]):
    index = key + 1  # потому что начинаем не с первого элемент
    if i < min_:
        min_ = i+1
        min_index = index
    elif i > max_:
        max_ = i+1
        max_index = index

array[min_index], array[max_index] = array[max_index], array[min_index]
print(array)
