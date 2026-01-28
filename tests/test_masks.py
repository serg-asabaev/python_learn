from src import masks

def test_get_mask_card_number_empty():
    assert masks.get_mask_card_number('') == ''


def test_get_mask_card_number():
    assert masks.get_mask_card_number('7000792289606361') == '7000 79** **** 6361 '
    assert masks.get_mask_card_number('7000792256168451') == '7000 79** **** 8451 '

def test_get_mask_account_empty():
    assert masks.get_mask_account('') == ''

def test_get_mask_account():
    assert masks.get_mask_account('73654108430135874305') == '**4305'
    assert masks.get_mask_account('73654108430135878643') == '**8643'