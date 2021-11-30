
def is_comparison_matrix(matrix_1, matrix_2):
    if not isinstance(matrix_1, Matrix):
        raise ValueError('Матрица 1 не является обьектом класса Matrix')
    elif not isinstance(matrix_2, Matrix):
        raise ValueError('Матрица 2 не является обьектом класса Matrix')
    elif len(matrix_1.list) != len(matrix_2.list):
        raise ValueError('Разное количество строк матриц')
    else:
        for key, value in enumerate(matrix_1.list):
            if len(value) != len(matrix_2.list[key]):
                raise ValueError(f'Разное количество элементов в строке {key+1}')

    return True


class Matrix:
    def __init__(self, lst_arg):
        self.list = lst_arg

    def __str__(self):
        result = ''
        for i_str in self.list:
            result += '\t'.join(map(str, i_str)) + '\n'
        return result

    def __add__(self, other):
        if is_comparison_matrix(self, other):
            new_m = list()
            for key_i, value_i in enumerate(self.list):
                new_m.append(list())
                for key_y, value_y in enumerate(value_i):
                    new_m[key_i].append(value_y + other.list[key_i][key_y])

            return Matrix(new_m)


m1 = Matrix([[31, 22], [37, 43], [51, 86]])
m2 = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
m3 = Matrix([[3, 5, 8, 3], [8, 3, 7, 1]])
m4 = Matrix([[1, 1, 1, 1], [1, 1, 1, 1]])

print(m1)
print(m2)
print(m3)
print(m4)

try:
    m1_2 = m1+m2
except ValueError as ve:
    print(ve)

try:
    m2_3 = m2+m3
except ValueError as ve:
    print(ve)

try:
    m = m2 + 4
except ValueError as ve:
    print(ve)

m3_4 = m3 + m4
print(m3_4)
