# import math
# import os
from typing import Union

# import requests

import masks
import widget
import proccessing


def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Функция которая складывает два числа"""

    return a + b


# print(add(5, 8))
# print(math.cos(2))

if __name__ == '__main__':

    print(masks.get_mask_card_number(''))

    print(masks.get_mask_account('73654108430135874305'))

    print(widget.mask_account_card("Счет 73654108430135874305"))
    print(widget.mask_account_card("Visa Platinum 7000792289606361"))

    print(widget.get_date("2024-03-11T02:26:18.671407"))
    # print(proccessing.filter_by_state([]))
    print(proccessing.filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                                       {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                                       {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                                       {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))