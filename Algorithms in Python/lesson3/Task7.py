# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

from random import randint as rint

SIZE = 10
MIN_ITEM = 1
MAX_ITEM = 10
array = [rint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

min_1, min_2 = array[0], array[1]

for i in array[2:]:
    if min_1 > i:
        min_1, min_2 = i, min_1 if min_1 < min_2 else min_2
    elif min_2 > i:
        min_2, min_1 = i, min_2 if min_2 < min_1 else min_1

print(min_1, min_2)
