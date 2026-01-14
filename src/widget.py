import masks


def mask_account_card(account_card: str) -> str:
    """ возвращает замаскированный номер карты или счета"""

    if len(account_card) == 0:
        return ""

    if account_card[:4] == "Счет":
        account_mask = account_card[:4] + " " + masks.get_mask_account(account_card[5:])
        return account_mask
    else:
        acc_card_name = account_card[:account_card.find(" " + account_card[-16:])]
        card_mask = acc_card_name + " " + masks.get_mask_card_number(account_card[-16:])
        return card_mask


def get_date(date_str: str) -> str:
    """ возвращает дату формата 2024-03-11T02:26:18.671407 в формате ДД.ММ.ГГГГ """

    if len(date_str) == 0:
        return ""

    date_res = ""

    date_res += date_str[8:10] + "."
    date_res += date_str[5:7] + "."
    date_res += date_str[:4]

    return date_res
