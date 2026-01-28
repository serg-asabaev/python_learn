# from src import main
from src import masks

def test_get_mask_card_number():
    assert masks.get_mask_card_number('7000792289606361') == '7000 79** **** 6361 '

