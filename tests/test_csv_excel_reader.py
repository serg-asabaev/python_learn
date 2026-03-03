from src.csv_excel_reader import read_csv, read_excel
from unittest.mock import patch
import pytest

@patch('src.csv_excel_reader.read_csv')
def test_read_csv(mock_read_csv, transactions_csv):
    mock_read_csv.return_value = transactions_csv
    assert read_csv('../data/transactions.csv')[0] == mock_read_csv.return_value


def test_read_csv_error():
    assert read_csv('../data/transactions1.csv') == []
    assert read_csv('data/transactions.csv') == []
    assert read_csv('../logs/transactions.csv') == []


def test_read_csv_empty():
    assert read_csv() == []
    assert read_csv('') == []

@patch('src.csv_excel_reader.read_excel')
def test_read_excel(mock_read_excel, transactions_exc):
    mock_read_excel.return_value = transactions_exc
    assert read_excel('../data/transactions_excel.xlsx')[0] == mock_read_excel.return_value

def test_read_excel_error():
    assert read_excel('../data/transactions_excel1.xlsx') == []
    assert read_excel('transactions_excel.xlsx') == []
    assert read_excel('../logs/transactions_excel.xlsx') == []

def test_read_excel_empty():
    assert read_excel() == []
    assert read_excel('') == []
