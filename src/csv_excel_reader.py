import csv

import pandas as pd


def read_csv(file_path: str = '') -> list[dict]:
    """Чтение CSV - файла"""

    if len(file_path) == 0:
        return []

    result = []

    try:
        with open(file_path, encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=";")

            for row in reader:
                row_dict = dict(row)
                result.append(row_dict)
    except Exception:
        return []

    return result


def read_excel(file_path: str = '') -> list[dict]:
    """Чтение Excel - файла"""

    if len(file_path) == 0:
        return []

    try:
        df = pd.read_excel(file_path, index_col=0)
        result = df.to_dict(orient="records")
    except Exception:
        return []

    return result
