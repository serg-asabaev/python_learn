import re
import pytest

from src.reg_exp_funcs import process_bank_search, process_bank_operations


@pytest.mark.parametrize('search_word, search_res', [
    ('Перевод организации', [{"id": 939719570,
                                "state": "EXECUTED",
                                "date": "2018-06-30T02:08:58.425572",
                                "operationAmount": {
                                    "amount": "9824.07",
                                    "currency": {
                                        "name": "USD",
                                        "code": "USD"
                                    }
                                },
                                "description": "Перевод организации",
                                "from": "Счет 75106830613657916952",
                                "to": "Счет 11776614605963066702"
                            },
                            {
                            "id": 594226727,
                            "state": "CANCELED",
                            "date": "2018-09-12T21:27:25.241689",
                            "operationAmount": {
                                "amount": "67314.70",
                                "currency": {
                                    "name": "руб.",
                                    "code": "RUB"
                                }
                            },
                            "description": "Перевод организации",
                            "from": "Visa Platinum 1246377376343588",
                            "to": "Счет 14211924144426031657"
                        }])
])
def test_process_bank_search(search_word, search_res, transactions):
    assert process_bank_search(transactions, search_word) == search_res


def test_process_bank_search_empty(transactions):
    assert process_bank_search([], '') == []
    assert process_bank_search([], 'Перевод организации') == []
    assert process_bank_search(transactions, '') == transactions


@pytest.mark.parametrize('categories, result', [
    (['Перевод организации', 'Перевод со счета на счет'],
     {'Перевод организации': 2, 'Перевод со счета на счет': 2})
])
def test_process_bank_operations(categories, result, transactions):
    assert process_bank_operations(transactions,categories) == result


def test_process_bank_operations_empty():
    assert process_bank_operations([],[]) == {}
    assert process_bank_operations([],['Перевод организации']) == {}
