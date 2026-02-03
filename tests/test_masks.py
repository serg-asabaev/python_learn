import pytest

from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number_empty():
    assert get_mask_card_number("") == ""


@pytest.mark.parametrize(
    "card_number, card_mask",
    [
        ("7000792289606361", "7000 79** **** 6361 "),
        ("7000792256168451", "7000 79** **** 8451 "),
    ],
)
def test_get_mask_card_number(card_number, card_mask):
    assert get_mask_card_number(card_number) == card_mask


def test_get_mask_account_empty():
    assert get_mask_account("") == ""


@pytest.mark.parametrize(
    "acc_number, acc_mask",
    [("73654108430135874305", "**4305"), ("73654108430135878643", "**8643")],
)
def test_get_mask_account(acc_number, acc_mask):
    assert get_mask_account(acc_number) == acc_mask
