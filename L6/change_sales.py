from pathlib import Path
from sys import argv

path_bakery_dir = Path.cwd() / 'L64'
path_bakery = path_bakery_dir / 'bakery.csv'
path_bakery_temp = path_bakery_dir / 'bakery_temp.csv'


def change(num_l, value_l):
    with path_bakery.open(encoding='utf-8', mode='tr') as f, path_bakery_temp.open(encoding='utf-8', mode='w') as f_new:
        for idx, line in enumerate(f):
            if idx+1 == num_l:
                f_new.write(f'{value_l}\n')
            else:
                f_new.write(line)
    path_bakery.unlink()
    path_bakery_temp.rename(path_bakery)


len_argv = len(argv)

if len_argv > 3:
    print('Не верное количество параметров')
    print(f'Для получения помощи укажите параметр "help"')
elif len_argv == 2 and argv[1].lower() == 'help':
    print('Скрипт получает два параметра: номер записи и новое значение')
else:
    num = 0
    value = 0
    if len_argv > 2 and (not argv[1].isdigit() or not argv[2].isdigit()):
        print('Не верное значение параметров')
        print(f'Для получения помощи укажите параметр "help"')
    elif len_argv > 1 and not argv[1].isdigit():
        print('Не верное значение параметров')
        print(f'Для получения помощи укажите параметр "help"')
    else:
        if len_argv > 1:
            num = int(argv[1])
        if len_argv > 2:
            value = int(argv[2])

        change(num, value)
