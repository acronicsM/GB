# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.

from random import randint


def merge_sort(in_array):
    size_array = len(in_array)  # Ускоряем вычисление(не вычисляем несколько раз)

    if size_array == 1:  # Массив из 1 элемента отсортирован
        return in_array

    midle_array = size_array // 2
    left = merge_sort(in_array[:midle_array])
    right = merge_sort(in_array[midle_array:])

    result = []
    i = j = 0
    size_l, size_r = len(left), len(right)

    while i < size_l and j < size_r:  # Цикл пока 1 из массивов не истощится
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])  # В конце остатки просто прибавляем к итоговому массиву
    result.extend(right[j:])

    return result


SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100

random_array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(random_array)

random_array = merge_sort(random_array)

print(random_array)
