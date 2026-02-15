def filter_by_state(input_list: list[dict], state: str = "EXECUTED") -> list[dict]:
    """возвращает новый список словарей, содержащий только те словари, у которых ключ state
    соответствует указанному значению
    """

    if len(input_list) == 0:
        return []

    if state == "":
        state = "EXPECTED"

    result_list = []

    for curr_dict in input_list:
        if curr_dict["state"] == state:
            result_list.append(curr_dict)

    return result_list


def sort_by_date(input_list: list[dict], order: bool = True) -> list[dict]:
    """сортирует по дате. по умолчанию - убывание, если order = False то возрастание"""

    if len(input_list) == 0:
        return []

    sorted_list = sorted(input_list, key=lambda x: x["date"], reverse=order)

    return sorted_list
