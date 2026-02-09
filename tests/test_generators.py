import pytest


from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

def test_filter_by_currency(transactions:list):
    filtered_list = filter_by_currency(transactions, 'USD')

    assert next(filtered_list) == {
          "id": 939719570,
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
      }

    assert next(filtered_list) == {
              "id": 142264268,
              "state": "EXECUTED",
              "date": "2019-04-04T23:20:05.206878",
              "operationAmount": {
                  "amount": "79114.93",
                  "currency": {
                      "name": "USD",
                      "code": "USD"
                  }
              },
              "description": "Перевод со счета на счет",
              "from": "Счет 19708645243227258542",
              "to": "Счет 75651667383060284188"
       }


def test_filter_by_currency_empty():
    filtered_list = filter_by_currency([], 'USD')

    assert next(filtered_list) == []


def test_transaction_descriptions(transactions:list):
    description = transaction_descriptions(transactions)

    assert next(description) == 'Перевод организации'
    assert next(description) == 'Перевод со счета на счет'
    assert next(description) == 'Перевод со счета на счет'
    assert next(description) == 'Перевод с карты на карту'


def test_transaction_descriptions():
    description = transaction_descriptions([])

    assert next(description) == ''


def test_card_number_generator():
    card_number = card_number_generator(1, 5)

    assert next(card_number) == '0000 0000 0000 0001'
    assert next(card_number) == '0000 0000 0000 0002'
    assert next(card_number) == '0000 0000 0000 0003'
    assert next(card_number) == '0000 0000 0000 0004'
    assert next(card_number) == '0000 0000 0000 0005'

def test_card_number_generator_zero():
    card_number = card_number_generator(0, 0)

    assert next(card_number) == ''

def test_card_number_generator_empty():
    card_number = card_number_generator()

    assert next(card_number) == ''