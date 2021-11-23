from pathlib import Path
import sys

path_bakery_dir = Path.cwd() / 'L64'
path_bakery = path_bakery_dir / 'bakery.csv'


def add(num):
    if not path_bakery_dir.exists():
        path_bakery_dir.mkdir()

    with path_bakery.open(encoding='utf-8', mode='a+') as f:
        f.write(f'{num}\n')


if len(sys.argv) < 2:
    print('Не указана сумма')
    print(f'Для получения помощи укажите параметр "help"')
elif len(sys.argv) > 3:
    print('Не верное количество параметров')
    print(f'Для получения помощи укажите параметр "help"')
elif sys.argv[1].lower() == 'help':
    print('Передайте в качестве единственного параметра целое число.')
elif not sys.argv[1].isdigit():
    print('В качестве параметра передана не сумма')
    print(f'Для получения помощи укажите параметр "help"')
else:
    add(sys.argv[1])
