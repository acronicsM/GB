# 4. Обработка списка чисел.
print('\nЗадание №4 ' + '<<'*20+'\n')

spis = [57.8, 46.40, 97, 12.3, 67.54, 8.07, 982.12, 1, 65, 9]

spis_str = ''
for i in spis:
    r, k = f'{i:.2f}'.split('.')
    spis_str = spis_str + f'{r} руб {k} коп,'

print(spis_str[:len(spis_str)-1])

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
