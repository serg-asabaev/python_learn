# import math
# import os
from typing import Union
import requests

from src import masks
from src import proccessing
from src import widget
from src.decorators import log
from src.utils import get_operations_list, get_transaction_sum
# from src.generators import card_number_generator, filter_by_currency
# from src.utils import get_operations_list, get_transaction_sum
from src.csv_excel_reader import read_csv, read_excel
# from tests.conftest import transactions



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

    # print(get_operations_list('data/operations.json'))
    # print(get_operations_list('operations.json'))
    operation =  {
        "id": 490100847,
        "state": "EXECUTED",
        "date": "2018-12-22T02:02:49.564873",
        "operationAmount": {
          "amount": "56516.63",
          "currency": {
            "name": "USD",
            "code": "USD"
          }
        },
        "description": "Перевод с карты на карту",
        "from": "Visa Gold 8326537236216459",
        "to": "MasterCard 6783917276771847"
      }

    # transactions = read_csv('data/transactions.csv')
    # print(transactions)
    # for tran in transactions:
    #     print(tran['from'])
    #

    excel_tran = read_excel('data/transactions_excel.xlsx')
    #
    print(excel_tran)
    # operttions_list = get_operations_list('data/operations.json')
    # print(operttions_list)