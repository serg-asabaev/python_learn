# import math
# import os
from typing import Union

# import requests

import masks


def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Функция которая складывает два числа"""

    return a + b


# print(add(5, 8))
# print(math.cos(2))

print(masks.get_mask_card_number(''))

print(masks.get_mask_account('73654108430135874305'))
