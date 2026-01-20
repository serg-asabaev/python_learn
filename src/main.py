# import math
# import os
from typing import Union

# import requests

import masks
import widget


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
    #test comment1