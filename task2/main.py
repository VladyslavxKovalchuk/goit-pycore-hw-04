# Функція get_cats_info(path) має приймати один аргумент - шлях до текстового файлу (path).
# Файл містить дані про котів, де кожен запис містить унікальний ідентифікатор, ім'я кота та його вік.
# Функція має повертати список словників, де кожен словник містить інформацію про одного кота.

from pathlib import Path


class FileCorruptedException(Exception):
    pass


def get_cats_info(path):
    filepath = Path(path)
    cats_infos = []
    if not filepath.exists():
        raise FileExistsError("Cats data file is not found")

    with open(path, "r") as cats_data:
        cats = cats_data.readlines()

    if len(cats) == 0:
        return []

    try:
        for cat in cats:
            cat_line_info = cat.split(",")
            cats_infos.append(
                {
                    "id": cat_line_info[0],
                    "name": cat_line_info[1],
                    "age": cat_line_info[2].strip(),
                }
            )

    except IndexError:
        raise FileCorruptedException(
            "Salary file corrupted or has unsupported structure"
        )
    except ValueError:
        raise FileCorruptedException(
            "Salary file corrupted or has unsupported structure"
        )
    return cats_infos


cats_info = get_cats_info("task2\data\cats.dat")
print(cats_info)
