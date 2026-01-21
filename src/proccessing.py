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