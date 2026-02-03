import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "date, formated_date",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2025-02-12T02:26:18.671407", "12.02.2025"),
        ("2026-01-11T02:26:18.671407", "11.01.2026"),
    ],
)
def test_get_date(date, formated_date):
    assert get_date(date) == formated_date


def test_get_date_empty():
    assert get_date("") == ""


@pytest.mark.parametrize(
    "card_num, card_mask",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361 "),
        ("Maestro 7000792289606361", "Maestro 7000 79** **** 6361 "),
        ("Mir 7000792289606361", "Mir 7000 79** **** 6361 "),
        ("Mir 7000792289605212", "Mir 7000 79** **** 5212 "),
    ],
)
def test_mask_account_card_card(card_num, card_mask):
    assert mask_account_card(card_num) == card_mask


def test_mask_account_card_account_empty():
    assert mask_account_card("") == ""


@pytest.mark.parametrize(
    "acc_num, acc_mask",
    [
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Счет 73654108430138548256", "Счет **8256"),
        ("Счет 73654108430135245256", "Счет **5256"),
        ("Счет 73654108430135251664", "Счет **1664"),
    ]
)
def test_mask_account_card_account(acc_num, acc_mask):
    assert mask_account_card(acc_num) == acc_mask
