import logging
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

# Создаем путь до файла логов относительно текущей директории
rel_file_path = os.path.join(current_dir, "../logs/masks.log")
abs_file_path = os.path.abspath(rel_file_path)


logger = logging.getLogger("masks_logger")
file_handler = logging.FileHandler(abs_file_path, encoding="utf-8", mode="w")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(funcName)s %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: str) -> str:
    """функция которая принимает на вход номер карты и возвращает ее маску"""

    logger.info("Начало маскировки карты")

    if len(card_number) == 0:
        logger.warning("Номер карты пустой!")
        return card_number

    card_mask = ""
    logger.info("Маскировка карты")

    for i in range(0, len(card_number)):
        ch = card_number[i]

        if 5 < i < len(card_number) - 4:
            ch = "*"

        if (i + 1) % 4 == 0:
            ch += " "

        card_mask += ch

    logger.info("Завершение маскировки карты")
    return card_mask


def get_mask_account(account_number: str) -> str:
    """функция которая принимает на вход номер счета и возвращает его маску"""
    logger.info("Начало маскировки счета")

    if len(account_number) == 0:
        logger.warning("Номер счета пустой!")
        return account_number

    logger.info("Маскировка счета")
    account_mask = "**" + account_number[-4:]

    logger.info("Конец маскировки счета")
    return account_mask
