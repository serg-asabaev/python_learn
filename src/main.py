# import math
# import os
from datetime import datetime
from itertools import chain
from typing import Union
import json

import pytest

from src import masks, proccessing, widget
from src.decorators import log
from src.generators import card_number_generator, filter_by_currency
from src.Utils import get_operations_list

# import requests


def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Функция которая складывает два числа"""

    return a + b


@log()
def subtract(x, y):
    return x - y


@log()
def multiply(x, y):
    return x * y


@log()
def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Деление на ноль невозможно")
    return x / y


def is_even(x: int) -> bool:
    return x % 2 == 0


def number_dup(x: Union[int, float]) -> list:
    return [x, x]


# print(add(5, 8))
# print(math.cos(2))

if __name__ == "__main__":

    print(get_operations_list('data/operations.json'))
    print(get_operations_list('operations.json'))