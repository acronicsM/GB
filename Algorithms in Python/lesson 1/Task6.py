# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

char_num = int(input('Введите номер буквы: '))

char_ = chr(char_num + 96)

print(f'Буква: {char_}')
