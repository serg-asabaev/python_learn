from src import widget
from src import masks

def test_get_date():
    assert widget.get_date('2024-03-11T02:26:18.671407') == '11.03.2024'
    assert widget.get_date('2025-02-12T02:26:18.671407') == '12.02.2025'
    assert widget.get_date('2026-01-11T02:26:18.671407') == '11.01.2026'

def test_get_date_empty():
    assert widget.get_date('') == ''

def test_mask_account_card_account():
    assert widget.mask_account_card('Visa Platinum 7000792289606361') == 'Visa Platinum 7000 79** **** 6361 '
    assert widget.mask_account_card('Maestro 7000792289606361') == 'Maestro 7000 79** **** 6361 '
    assert widget.mask_account_card('Mir 7000792289606361') == 'Mir 7000 79** **** 6361 '

    assert widget.mask_account_card('Mir 7000792289605212') == 'Mir 7000 79** **** 5212 '

def test_mask_account_card_account_empty():
    assert widget.mask_account_card('') == ''