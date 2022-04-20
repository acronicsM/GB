# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
# Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
#
# Примечание: задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, используйте метод сортировки, который не рассматривался на уроках
# (сортировка слиянием также недопустима).

from random import randint, choice


def median(arr, pivot_number=None):

    if pivot_number is None:
        pivot_number = len(arr) // 2 + 1

    if len(arr) == 1:
        return arr[0]

    pivot = choice(arr)
    l_arr = [i for i in arr if i < pivot]
    r_arr = [i for i in arr if i > pivot]
    p_arr = [i for i in arr if i == pivot]

    size_l = len(l_arr)
    size_p = len(p_arr)

    if pivot_number < size_l:
        return median(l_arr, pivot_number)
    elif pivot_number < (size_l + size_p):
        return pivot
    else:
        return median(r_arr, pivot_number - size_l - size_p)


SIZE = int(input('Введите  натурильное число: '))
MIN_ITEM = -10
MAX_ITEM = 10

random_array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(2*SIZE + 1)]

print(random_array)
print(median(random_array))
