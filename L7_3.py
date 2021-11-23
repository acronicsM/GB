from pathlib import Path
from os import walk
from shutil import copytree
from L7_2 import create_map

create_map(Path.cwd() / 'task_3', Path.cwd() / 'task_2' / 'config_2.yaml')

path_dir = Path.cwd() / 'task_3' / 'my_project'

for root, *i in walk(path_dir):
    if root.endswith('templates'):
        copytree(root, path_dir / 'templates', dirs_exist_ok=True)
