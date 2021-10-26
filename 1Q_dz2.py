
# 1. Выяснить тип результата следующих выражений:
print('\nЗадание №1 ' + '<<'*20+'\n')

print(f' 15 * 3 тип {type(15 * 3)}')
print(f' 15 * 3 тип {type(15 / 3)}')
print(f' 15 * 3 тип {type(15 // 2)}')
print(f' 15 * 3 тип {type(15 ** 3)}')

# 2. Дан список строк.
print('\nЗадание №2 ' + '<<'*20+'\n')

str = ['dfdf','7', 'в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', '-7', 'градусов', '9']
str_new = ''
maxlen = len(str)-1
pred_isdigit = False

for i in range(maxlen,-1,-1):
    elem = str[i]

    if pred_isdigit:
        str.insert(i + 1, '"')
        pred_isdigit = False

    if elem.lstrip('-+').isdigit():
        str.insert(i+1,'"')
        pred_isdigit = True

maxlen = len(str)-1
for i, elem in enumerate(str):
    if elem.lstrip('-+').isdigit():
        str_new = str_new + elem
    elif i<maxlen and elem == '"' and str[i+1].lstrip('-+').isdigit():
        str_new = str_new + elem
    else:
        str_new = str_new + elem + ' '

str_new = str_new.strip()

print(str)
print(str_new)

# 3. Дан список, содержащий искаженные данные с должностями и именами сотрудников
print('\nЗадание №3 ' + '<<'*20+'\n')

str = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for i in str:
    print(f'Привет, {i.split()[-1].capitalize()}!')

# 4. Обработка списка чисел.
print('\nЗадание №4 ' + '<<'*20+'\n')

spis = [57.8, 46.40, 97, 12.3, 67.54, 8.07, 982.12, 1, 65, 9]

str = ''
for i in spis:
    r,k = f'{i:.2f}'.split('.')
    str = str + f'{r} руб {k} коп,'

print(str[:len(str)-1])

print(spis)
print(f'id до сортировки ДО возрастанию {id(spis)}')
spis.sort()
print(spis)
print(f'id до сортировки ПОСЛЕ возрастанию {id(spis)}')

spis_r = spis.copy()
spis_r.reverse()
print(spis_r)
print(f'id до сортировки ПОСЛЕ убывания {id(spis_r)}')

print('5 самых дорогих товаров:')
a = spis_r[:5]
print(spis_r[:5])
