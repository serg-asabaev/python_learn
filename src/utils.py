import json
import logging
import os

from src.external_api import get_rouble_amount
from tests.conftest import operation

current_dir = os.path.dirname(os.path.abspath(__file__))


# Создаем путь до файла логов относительно текущей директории
rel_file_path = os.path.join(current_dir, "../logs/utils.log")
abs_file_path = os.path.abspath(rel_file_path)

logger = logging.getLogger("utils_logger")
file_handler = logging.FileHandler(abs_file_path, encoding="utf-8", mode="w")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_operations_list(file: str = "") -> list[dict]:
    """Получение json-обьекта из указанного файла"""
    logger.info("Начало работы функции get_operations_list")

    if len(file) == 0:
        logger.warning("не указан путь до файла")
        return []

    try:
        logger.info("Начало получения данных")
        with open(file, "r", encoding="utf-8") as f:
            json_obj = list(json.load(f))
            logger.info("получение данных завершено успешно")
    except FileNotFoundError:
        logger.error("файл не найден")
        return []
    except json.JSONDecodeError:
        logger.error("содержимое файла не является json-объектом")
        return []
    except TypeError:
        logger.error("ошибка распознавания содержимого файла")
        return []
    except KeyError:
        logger.error("не найден ключ в файле")
        return []
    except ValueError:
        logger.error("ошибка значения файла")
        return []

    logger.info("Завершение работы функции get_operations_list")
    return json_obj


def get_transaction_sum(transaction: dict = {}) -> float:
    """Получение суммы в рублях из входящего словаря транзакции"""
    logger.info("Начало работы функции get_transaction_sum")

    if (
        len(transaction) == 0
        or "operationAmount" not in transaction
        or "amount" not in transaction["operationAmount"]
        or "currency" not in transaction["operationAmount"]
        or "code" not in transaction["operationAmount"]["currency"]
    ):
        logger.warning("не указаны входные данные")
        return 0

    logger.info("Получение входных данных")
    amount = float(transaction["operationAmount"]["amount"])
    currency = transaction["operationAmount"]["currency"]["code"]

    if currency == "RUB":
        logger.info("Завершение работы функции get_transaction_sum сумма в рублях")
        return amount
    else:
        logger.info("сумма в валюте получение суммы в рублях")

        # try:
        result = get_rouble_amount(amount, currency)
        logger.info("данные получены")
        # except Exception:
        #     logger.error("ошибка получения данных")
        #     return Exception

        logger.info("Завершение работы функции get_transaction_sum ")
        return result