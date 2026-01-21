def filter_by_state(input_list: list[dict], _state_: str = 'EXECUTED') -> list[dict]:
    """  возвращает новый список словарей, содержащий только те словари, у которых ключ state
            соответствует указанному значению
    """

    if len(input_list) == 0:
        return []

    result_list = []
    state = _state_

    for curr_dict in input_list:
        if curr_dict['state'] == state:
            result_list.append(curr_dict)

    return result_list

def sort_by_date(input_list: list[dict], _order: bool = True) -> list[dict]:
    """ сортирует по дате. по умолчанию - убывание, если _order = 1 то возрастание """

    if len(input_list) == 0:
        return []

    order = _order

    sorted_list = sorted(input_list, key=lambda x: x['date'], reverse=order)

    return sorted_list