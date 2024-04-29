# Функція total_salary(path) має приймати один аргумент - шлях до текстового файлу (path).
# Файл містить дані про заробітні плати розробників, розділені комами. Кожен рядок вказує на одного розробника.
# Функція повинна аналізувати файл, обчислювати загальну та середню суму заробітної плати.
# Результатом роботи функції є кортеж із двох чисел: загальної суми зарплат і середньої заробітної плати.


# Оскільки сума зарплати може бути не цілочисленою, використав тип float.

from pathlib import Path


class FileCorruptedException(Exception):
    pass


def total_salary(path):
    salaries = []
    TotalSalary = 0.0
    filepath = Path(path)
    if not filepath.exists():
        raise FileExistsError("Salary file is not found")

    with open(path, "r") as salarydata:
        salaries = salarydata.readlines()

    if len(salaries) == 0:
        return {0.0, 0.0}

    try:
        for salary_line in salaries:
            TotalSalary += float(salary_line.split(",")[1])

    except IndexError:
        raise FileCorruptedException(
            "Salary file corrupted or has unsupported structure"
        )
    except ValueError:
        raise FileCorruptedException(
            "Salary file corrupted or has unsupported structure"
        )

    return {TotalSalary, TotalSalary / len(salaries)}
