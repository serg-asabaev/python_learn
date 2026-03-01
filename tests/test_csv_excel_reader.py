from src.csv_excel_reader import read_csv, read_excel
from unittest.mock import patch
import pytest

def test_read_csv(transactions_csv_exc):
    csv_info_first = read_csv('../data/transactions.csv')[0]
    assert csv_info_first == transactions_csv_exc


def test_read_csv_error():
    assert read_csv('../data/transactions1.csv') == []
    assert read_csv('data/transactions.csv') == []
    assert read_csv('../logs/transactions.csv') == []


def test_read_csv_empty():
    assert read_csv() == []
    assert read_csv('') == []