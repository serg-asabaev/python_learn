from unittest.mock import patch, Mock, ANY
import requests
import pytest


from src.utils import get_operations_list, get_transaction_sum
from src.external_api import get_rouble_amount

def test_get_operations_list(operations):
    assert get_operations_list('../data/operations.json') == operations


def test_get_operations_list_error():
    assert get_operations_list('../data/operations.json') == []
    assert get_operations_list('') == []


def test_get_operations_list_empty():
    assert get_operations_list() == []

@patch('requests.get')
def test_get_transaction_sum(mock_get, operation):
    currency = operation["operationAmount"]["currency"]["code"]
    amount = operation["operationAmount"]["amount"]

    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"result": 4326679.835635}

    assert get_rouble_amount(amount, currency) == 4326679.835635
    mock_get.assert_called_once_with(
        f"https://api.apilayer.com/currency_data/convert?to=RUB&from={currency}&amount={amount}",
        headers={'apikey': ANY}
    )


def test_get_transaction_sum_error(wrong_operation):
    assert get_transaction_sum({}) == 0
    assert get_transaction_sum(wrong_operation) == 0


def test_get_transaction_sum_empty():
    assert get_transaction_sum() == 0