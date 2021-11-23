from pathlib import Path


def create_map(path_dir, dir_map):
    chet = 0
    new_dir = path_dir
    with dir_map.open(encoding='utf-8', mode='tr') as f_dir_map:
        for line in f_dir_map:
            idx_find = line.find('- ')
            name_dir = line.rstrip().rstrip(':').lstrip('- ')

            if line.find('.') != -1:  # Если есть точка, то это файл
                (new_dir / name_dir).touch(exist_ok=True)
            else:
                idx = 0 if idx_find == -1 else int(idx_find / 2)
                if idx < chet:
                    for x in range(chet - idx):
                        new_dir = new_dir.parent
                    chet = idx

                chet += 1
                new_dir = new_dir / name_dir
                new_dir.mkdir(exist_ok=True)


if __name__ == "__main__":
    create_map(Path.cwd() / 'task_2', Path.cwd() / 'task_2' / 'config_2.yaml')
