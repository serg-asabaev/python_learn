from typing import Generator


def filter_by_currency(input_list: list, currency: str) -> Generator:
    """Функция возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной"""
    if len(input_list) == 0:
        yield []

    for curr_dict in input_list:
        if curr_dict == {}:
            continue
        try:
            if curr_dict["operationAmount"]["currency"]["code"] == currency:
                res = curr_dict
                yield res
        except KeyError:
            if curr_dict["currency_code"] == currency:
                res = curr_dict
                yield res


def transaction_descriptions(input_list: list) -> Generator:
    """принимает список словарей с транзакциями и возвращает описание каждой операции по очереди"""
    if len(input_list) == 0:
        yield ""

    for curr_dict in input_list:
        yield str(curr_dict["description"])


def card_number_generator(beg_number: int = 0, end_number: int = 0) -> Generator:
    """
    Генератор который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где
    X — цифра номера карты
    """

    if beg_number == 0 or end_number == 0:
        yield ""

    for i in range(beg_number, end_number + 1):
        card_number = ""
        card_number_str = "0000000000000000" + str(i)
        card_number_str = card_number_str[-16:]

        for j in range(0, len(card_number_str)):
            if (j + 1) % 4 == 0 and j < len(card_number_str) + 1:
                card_number += str(card_number_str[j]) + " "
            else:
                card_number += str(card_number_str[j])

        yield card_number[: len(card_number) - 1]
