from unittest.mock import patch, Mock
import requests

from src.utils import get_operations_list, get_transaction_sum
from src.external_api import get_rouble_amount


def test_get_operations_list(operations):
    assert get_operations_list('../data/operations.json') == operations


def test_get_operations_list_error():
    assert get_operations_list('/src/operations.json') == []
    assert get_operations_list('') == []


def test_get_operations_list_empty():
    assert get_operations_list() == []


@patch('requests.get')
def test_get_transaction_sum(mock_get, operation, currencies):
    mock_get.return_value.json.return_value = currencies

    assert get_transaction_sum(operation) == 76.7519 * float(operation["operationAmount"]["amount"])
    mock_get.assert_called_once_with('https://www.cbr-xml-daily.ru/daily_json.js')

def test_get_transaction_sum_error(wrong_operation):
    assert get_transaction_sum({}) == 0
    assert get_transaction_sum(wrong_operation) == 0


def test_get_transaction_sum_empty():
    assert get_transaction_sum() == 0