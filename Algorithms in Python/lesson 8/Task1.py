# Определение количества различных подстрок с использованием хеш-функции.
# Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.
# Пример работы функции:
#
# >>> func("papa")
# 6
# >>> func("sova")
# 9

def number_of_substrings(s):
    return len({hash(s[i:j]) for i in range(len(s)) for j in range(i + 1, len(s) + 1) if j < len(s) + i})


print(number_of_substrings('papa'))
print(number_of_substrings('sova'))
