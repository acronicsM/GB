from pathlib import Path
from os import walk, stat

sizes = dict()
for roots, dirs, files in walk(Path.cwd() / 'task_4'):
    if files:
        for i in files:
            size = stat(Path(roots) / i).st_size
            capacity = '1' + '0'*len(str(size))

            if sizes.get(capacity) is None:
                sizes[capacity] = 1
            else:
                sizes[capacity] += 1

print(sizes)
