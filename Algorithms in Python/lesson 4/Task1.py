# Определить, какое число в массиве встречается чаще всего.

from random import randint as rint
from timeit import timeit as tit
from cProfile import run as cPrun
import collections


def rnd(size):
    MIN_ITEM = 0
    MAX_ITEM = 100
    return [rint(MIN_ITEM, MAX_ITEM) for _ in range(size)]


def majority(size):
    res = {}
    max_i = 0
    max_ = None

    for i in rnd(size):
        if res.get(i) is None:
            res[i] = 1
        else:
            res[i] += 1

    for key, i in res.items():
        if max_ is None:
            max_i = key
            max_ = i
        elif max_ < i:
            max_i = key
            max_ = i

    return max_i, max_


def majority2(size):
    array = rnd(size)
    len_ = len(array)
    num = array[0]
    max_frq = 1
    for i in range(len_ - 1):
        frq = 1
        for k in range(i + 1, len_):
            if array[i] == array[k]:
                frq += 1
        if frq > max_frq:
            max_frq = frq
            num = array[i]

    return num, max_frq


def majority3(size):
    res = collections.Counter(rnd(size)).most_common()
    return res[0][0], res[0][1]


print(tit('majority(10)', number=1000, globals=globals()))      # 0.01100980001501739
print(tit('majority(100)', number=1000, globals=globals()))     # 0.08689890010282397
print(tit('majority(1000)', number=1000, globals=globals()))    # 0.7671344999689609
print(tit('majority(10000)', number=1000, globals=globals()))   # 7.383771400200203
print(tit('majority(100000)', number=1000, globals=globals()))  # 72.50877950014547

cPrun('majority(100000)')

# 926887 function calls in 0.312 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.312    0.312 <string>:1(<module>)
#         1    0.021    0.021    0.225    0.225 Task1.py:11(<listcomp>)
#         1    0.073    0.073    0.312    0.312 Task1.py:13(majority)
#         1    0.000    0.000    0.225    0.225 Task1.py:8(rnd)
#    100000    0.049    0.000    0.069    0.000 random.py:239(_randbelow_with_getrandbits)
#    100000    0.083    0.000    0.174    0.000 random.py:292(randrange)
#    100000    0.029    0.000    0.204    0.000 random.py:366(randint)
#    300000    0.023    0.000    0.023    0.000 {built-in method _operator.index}
#         1    0.000    0.000    0.312    0.312 {built-in method builtins.exec}
#    100000    0.008    0.000    0.008    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#    100000    0.014    0.000    0.014    0.000 {method 'get' of 'dict' objects}
#    126880    0.012    0.000    0.012    0.000 {method 'getrandbits' of '_random.Random' objects}
#         1    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}

print(tit('majority2(10)', number=1000, globals=globals()))      # 0.016219499986618757
print(tit('majority2(100)', number=1000, globals=globals()))     # 0.35527329985052347
print(tit('majority2(1000)', number=1000, globals=globals()))    # 28.192921800073236

cPrun('majority2(2000)')

    #     16536 function calls in 0.112 seconds
    #
    # Ordered by: standard name
    #
    # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    #      1    0.000    0.000    0.112    0.112 <string>:1(<module>)
    #      1    0.000    0.000    0.004    0.004 Task1.py:10(<listcomp>)
    #      1    0.108    0.108    0.112    0.112 Task1.py:33(majority2)
    #      1    0.000    0.000    0.004    0.004 Task1.py:7(rnd)
    #   2000    0.001    0.000    0.001    0.000 random.py:239(_randbelow_with_getrandbits)
    #   2000    0.002    0.000    0.003    0.000 random.py:292(randrange)
    #   2000    0.001    0.000    0.004    0.000 random.py:366(randint)
    #   6000    0.000    0.000    0.000    0.000 {built-in method _operator.index}
    #      1    0.000    0.000    0.112    0.112 {built-in method builtins.exec}
    #      1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
    #   2000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
    #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    #   2529    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

print(tit('majority3(10)', number=1000, globals=globals()))     # 0.00928230001591146
print(tit('majority3(100)', number=1000, globals=globals()))    # 0.07429679995402694
print(tit('majority3(1000)', number=1000, globals=globals()))   # 0.659322899999097
print(tit('majority3(10000)', number=1000, globals=globals()))  # 6.403295899974182
print(tit('majority3(100000)', number=1000, globals=globals())) # 65.2911014999263

cPrun('majority3(100000)')

   #       826931 function calls (826923 primitive calls) in 0.238 seconds
   #
   # Ordered by: standard name
   #
   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #      1    0.000    0.000    0.238    0.238 <string>:1(<module>)
   #      1    0.022    0.022    0.234    0.234 Task1.py:11(<listcomp>)
   #      1    0.000    0.000    0.238    0.238 Task1.py:50(majority3)
   #      1    0.000    0.000    0.234    0.234 Task1.py:8(rnd)
   #      1    0.000    0.000    0.003    0.003 __init__.py:565(__init__)
   #      1    0.000    0.000    0.000    0.000 __init__.py:588(most_common)
   #      1    0.000    0.000    0.003    0.003 __init__.py:640(update)
   #      5    0.000    0.000    0.000    0.000 _collections_abc.py:409(__subclasshook__)
   #      1    0.000    0.000    0.000    0.000 abc.py:117(__instancecheck__)
   #    5/1    0.000    0.000    0.000    0.000 abc.py:121(__subclasscheck__)
   # 100000    0.050    0.000    0.071    0.000 random.py:239(_randbelow_with_getrandbits)
   # 100000    0.088    0.000    0.183    0.000 random.py:292(randrange)
   # 100000    0.029    0.000    0.212    0.000 random.py:366(randint)
   #      1    0.000    0.000    0.000    0.000 {built-in method _abc._abc_instancecheck}
   #    5/1    0.000    0.000    0.000    0.000 {built-in method _abc._abc_subclasscheck}
   #      1    0.003    0.003    0.003    0.003 {built-in method _collections._count_elements}
   # 300000    0.024    0.000    0.024    0.000 {built-in method _operator.index}
   #      1    0.000    0.000    0.238    0.238 {built-in method builtins.exec}
   #      1    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
   #      1    0.000    0.000    0.000    0.000 {built-in method builtins.sorted}
   # 100000    0.008    0.000    0.008    0.000 {method 'bit_length' of 'int' objects}
   #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
   # 126901    0.012    0.000    0.012    0.000 {method 'getrandbits' of '_random.Random' objects}
   #      1    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}


# Выводы:
# Наилучшую производительность показал метод majority3 в котором используется функция Counter модуля collections
# На втором месте метод majority который схож с функцией Counter модуля collections но не использует C
# Наихудшие результаты оказались у метода majority, что обьясняется вложенным циклом

