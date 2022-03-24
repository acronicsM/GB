# В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
# Это два абсолютно разных значения.
from random import randint as rint

SIZE = 10
MIN_ITEM = -10
MAX_ITEM = 10
array = [rint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

ind = 0
max_ = array[ind]

for key, i in enumerate(array[1:]):
    if i < 0 and (max_ > 0 or i > max_):
        max_ = i
        ind = key + 1

if max_ > 0:
    print('Отрицательных элементов в массиве нет')
else:
    print(f'максимальный отрицательный элемент {max_} по индексу {ind}')
