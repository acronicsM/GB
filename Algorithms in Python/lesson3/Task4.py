# Определить, какое число в массиве встречается чаще всего.

from random import randint as rint
from time import perf_counter as pcnt

SIZE = 10
MIN_ITEM = 3
MAX_ITEM = 6
array = [rint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

tic = pcnt()
res = {}
for i in array:
    if res.get(i) is None:
        res[i] = 1
    else:
        res[i] += 1

max_i = 0
max_ = None

for key, i in res.items():
    if max_ is None:
        max_i = key
        max_ = i
    elif max_ < i:
        max_i = key
        max_ = i

print(f'число {max_i} встречается максимальное число раз ({max_})')
print(f"Вычисление заняло {pcnt() - tic:0.4f} секунд")

# БЕЗУМНО МЕДЛЕННО
# tic = pcnt()
# len_ = len(array)
# num = array[0]
# max_frq = 1
# for i in range(len_ - 1):
#     frq = 1
#     for k in range(i+1,len_):
#         if array[i] == array[k]:
#             frq += 1
#     if frq > max_frq:
#         max_frq = frq
#         num = array[i]
#
# print(f'число {num} встречается максимальное число раз ({max_frq})')
# print(f"Вычисление заняло {pcnt() - tic:0.4f} секунд")
