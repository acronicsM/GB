from pathlib import Path
from os import walk, stat
from json import dump

dir_path = Path.cwd() / 'task_5'
sizes = dict()
for roots, dirs, files in walk(dir_path):
    if files:
        for i in files:
            path_i = Path(roots) / i
            size = stat(path_i).st_size
            suffix = path_i.suffix.lstrip('.')
            capacity = '1' + '0'*len(str(size))

            if sizes.get(capacity) is None:
                sizes[capacity] = [1, [suffix]]
            else:
                sizes[capacity][0] += 1
                if suffix not in sizes[capacity][1]:
                    sizes[capacity][1].append(suffix)

name_json = Path.cwd() / f'{Path.cwd().name}_summary.json'
with name_json.open(encoding='utf=8', mode='w') as f_new:
    dump(sizes, f_new, indent=2)
