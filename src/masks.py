

def get_mask_card_number(card_number: str) -> str:
    """ функция которая принимает на вход номер карты и возвращает ее маску """

    if len(card_number) == 0:
        return card_number

    card_mask = ""

    for i in range(0, len(card_number)):
        ch = card_number[i]

        if 5 < i < len(card_number) - 4:
            ch = "*"

        if (i + 1) % 4 == 0:
            ch += " "

        card_mask += ch

    return card_mask


def get_mask_account(account_number: str) -> str:
    """ функция которая принимает на вход номер счета и возвращает его маску """

    if len(account_number) == 0:
        return account_number

    account_mask = "**" + account_number[-4:]

    return account_mask
