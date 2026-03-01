from src.csv_excel_reader import read_csv, read_excel
from unittest.mock import patch
import pytest

def test_read_csv(transactions_csv_exc):
    assert read_csv('../data/transactions.csv')[0] == transactions_csv_exc


def test_read_csv_error():
    pass


def test_read_csv_empty():
    pass