import re
from collections import Counter

from tests.conftest import transactions


def process_bank_search(data:list[dict], search:str)->list[dict]:
    """ Поиск по подстроке в описании, возвращает список найденных операций """

    if len(data) == 0:
        return []

    result = []
    pattern = rf'({search})'

    for process in data:
        description = process['description']
        # result.append(re.findall(pattern, description))

        if len(re.findall(pattern, description)) > 0:
            result.append(process)

    return result

def process_bank_operations(data:list[dict], categories:list)->dict:
    """
        Подсчет количества операций по категориям поданным на вход, возвращает словарь,
        где ключ это категория, а значение - количество операций с данной категорией
    """

    if len(data) == 0:
        return {}

    opers_in_categories = []

    for operation in data:
        if operation['description'] in categories:
            opers_in_categories.append(operation['description'])

    return dict(Counter(opers_in_categories))
