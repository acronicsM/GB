import sys
from pathlib import Path

path_bakery_dir = Path.cwd() / 'L64'
path_bakery = path_bakery_dir / 'bakery.csv'


def show(start_l=0, stop_l=0):
    with path_bakery.open(encoding='utf-8', mode='tr') as f:
        for idx, line in enumerate(f):
            if start_l and idx+1 < start_l:
                continue
            elif stop_l and idx >= stop_l:
                break
            print(line.rstrip())


len_argv = len(sys.argv)

if len_argv > 3:
    print('Не верное количество параметров')
    print(f'Для получения помощи укажите параметр "help"')
elif len_argv == 2 and sys.argv[1].lower() == 'help':
    print('просто запуск скрипта — выводить все записи')
    print('запуск скрипта с одним параметром-числом — выводить все записи от номера, равного этому числу, до конца;')
    print('запуск скрипта с двумя числами — выводить записи, начиная от номера, равного первому числу, '
          'по номер равный второму числу, включительно;')
else:
    start = 0
    stop = 0
    if len_argv > 2 and (not sys.argv[1].isdigit() or not sys.argv[2].isdigit()):
        print('Не верное значение параметров')
        print(f'Для получения помощи укажите параметр "help"')
        exit()
    elif len_argv > 1 and not sys.argv[1].isdigit():
        print('Не верное значение параметров')
        print(f'Для получения помощи укажите параметр "help"')
        exit()
    else:
        if len_argv > 1:
            start = int(sys.argv[1])
        if len_argv > 2:
            stop = int(sys.argv[2])

        show(start, stop)
