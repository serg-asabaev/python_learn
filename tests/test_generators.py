import pytest


from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

@pytest.mark.parametrize('result1, result2, result3', [
    ({
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        }
    ),
])
def test_filter_by_currency(transactions:list, result1, result2, result3):
    filtered_list = filter_by_currency(transactions, "USD")

    assert next(filtered_list) == result1
    assert next(filtered_list) == result2
    assert next(filtered_list) == result3


def test_filter_by_currency_empty():
    filtered_list = filter_by_currency([], 'USD')

    assert next(filtered_list) == []

@pytest.mark.parametrize('result1, result2, result3', [
    ('Перевод организации',
    'Перевод со счета на счет',
    'Перевод с карты на карту'),
])
def test_transaction_descriptions(transactions:list, result1, result2, result3):
    description = transaction_descriptions(transactions)

    assert next(description) == result1
    assert next(description) == result2
    assert next(description) == result2
    assert next(description) == result3


def test_transaction_descriptions_empty():
    description = transaction_descriptions([])

    assert next(description) == ''

@pytest.mark.parametrize("beg_int, end_int, result1, result2, result3, result4, result5", [
    (1, 5, '0000 0000 0000 0001', '0000 0000 0000 0002', '0000 0000 0000 0003', '0000 0000 0000 0004', '0000 0000 0000 0005'),
])
def test_card_number_generator(beg_int, end_int, result1, result2, result3, result4, result5):
    card_number = card_number_generator(1, 5)
    assert next(card_number) == result1
    assert next(card_number) == result2
    assert next(card_number) == result3
    assert next(card_number) == result4
    assert next(card_number) == result5

def test_card_number_generator_zero():
    card_number = card_number_generator(0, 0)

    assert next(card_number) == ''

def test_card_number_generator_empty():
    card_number = card_number_generator()

    assert next(card_number) == ''