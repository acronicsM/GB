from pathlib import Path


def create_dir(parent, dirs):
    for i in dirs:
        new_dir = parent / i
        new_dir.mkdir(exist_ok=True)
        if not dirs[i] is None:
            create_dir(new_dir, dirs[i])


if __name__ == "__main__":
    map_dir = {
        "my_project": {
            "mainapp": None,
            "adminapp": None,
            "authapp": None
        }
    }

    create_dir(Path.cwd() / 'task_1', map_dir)
