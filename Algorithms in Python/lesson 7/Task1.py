# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Примечания:
# ● алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
# ● постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
#       Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.

from random import randint


def bubble(in_array):
    doit = True  # Сокращаем расходы памяти и время на вычисление
    s_array = len(in_array)
    num_iter = 0
    while doit:
        doit = False
        for i in range(s_array - num_iter - 1):  # Нет смысла пробигать весь массив, конец уже отсортирован
            if in_array[i + 1] > in_array[i]:
                in_array[i + 1], in_array[i] = in_array[i],  in_array[i + 1]
                doit = True
        num_iter += 1
        print(in_array)


SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100

random_array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(random_array)

bubble(random_array)

print(random_array)
