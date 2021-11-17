from pathlib import Path
from json import dump

path_dir = Path.cwd() / 'data' / 'L63'
path_hobby = path_dir / 'task_3_hobby.csv'
path_users = path_dir / 'task_3_users.csv'
path_rezult = path_dir / 'task_3_rezult.txt'

users = list()
max_hobby = 0

if path_hobby.exists() and path_users.exists() and path_hobby.is_file() and path_hobby.is_file():
    with path_hobby.open(encoding='utf-8', mode='tr') as f_hobby:
        str_hobby = f_hobby.readlines()
        max_hobby = len(str_hobby)
    with path_users.open(encoding='utf-8', mode='tr') as f_users:
        for x in f_users.readlines():
            fio = x.split(',')
            users.append(f'{fio[0][0]}{fio[1][0]}{fio[2][0]}')

result = {x: str_hobby[idx].rstrip() if idx < max_hobby else None for idx, x in enumerate(users)}

with path_rezult.open(mode='w') as write_file:
    dump(result, write_file, indent=2, ensure_ascii=False)

if len(users) < max_hobby:
    exit(1)
