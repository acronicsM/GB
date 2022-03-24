# Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
# второй массив надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.

from random import randint as rint
from time import perf_counter as pcnt

SIZE = 10
MIN_ITEM = 2
MAX_ITEM = 99
array = [rint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

tic = pcnt()
arr_res2 = [key for key, i in enumerate(array) if not i % 2]

print(arr_res2)
print(f"Вычисление заняло {pcnt() - tic:0.4f} секунд")

# МЕДЛЕНО
# tic = pcnt()
# arr_res = []
#
# ind = 0
# for i in array:
#     if i % 2 == 0:
#         arr_res.append(ind)
#     ind += 1
#
# print(arr_res)
# print(f"Вычисление заняло {pcnt() - tic:0.4f} секунд")
