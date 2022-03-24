# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

from random import randint as rint

SIZE = 10
MIN_ITEM = 1
MAX_ITEM = 10
array = [rint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

summ = 0
min_index = max_index = 0
min_ = max_ = array[min_index]

for key, i in enumerate(array[1:]):
    index = key + 1  # потому что начинаем не с первого элемент
    if i < min_:
        min_ = i
        min_index = index
    elif i > max_:
        max_ = i
        max_index = index

ratio = 1 if min_index < max_index else -1
for i in array[min_index + ratio: max_index: ratio]:
    summ += i

print(min_ , max_)
print(min_index , max_index)
print(summ)
