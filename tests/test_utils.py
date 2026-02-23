from unittest.mock import patch, Mock
import requests
import pytest
from src.external_api import get_rouble_amount

from src.utils import get_operations_list, get_transaction_sum
from src.external_api import get_rouble_amount


def test_get_operations_list(operations):
    assert get_operations_list('../data/operations.json') == operations


def test_get_operations_list_error():
    assert get_operations_list('/src/operations.json') == []
    assert get_operations_list('') == []


def test_get_operations_list_empty():
    assert get_operations_list() == []


# @patch('external_api.get_rouble_amount')
def test_get_transaction_sum(mock_get, operation):

    currency = operation["operationAmount"]["currency"]["code"]
    amount = operation["operationAmount"]["amount"]

    mock_get = Mock(return_value=4346675.927978)
    get_rouble_amount = mock_get
    print(get_transaction_sum(operation))
    print(get_transaction_sum(operation))
    print(get_transaction_sum(operation))

    params = f'?to=RUB&from={currency}&amount={amount}'
    assert get_transaction_sum(operation) == mock_get
    mock_get.assert_called_once_with(f'https://api.apilayer.com/currency_data/convert{params}')


def test_get_transaction_sum_error(wrong_operation):
    assert get_transaction_sum({}) == 0
    assert get_transaction_sum(wrong_operation) == 0


def test_get_transaction_sum_empty():
    assert get_transaction_sum() == 0