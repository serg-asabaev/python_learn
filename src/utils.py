import json
import logging
from mypy.types_utils import UnionType

from src.external_api import get_rouble_amount
from tests.conftest import operation


logger = logging.getLogger('utils_logger')
file_handler = logging.FileHandler('../logs/utils.log', encoding='utf-8', mode='w')
file_formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)

def get_operations_list(file: str = '') -> list[dict]:
    """ Получение json-обьекта из указанного файла """
    logger.info('Начало маскировки карты')

    if len(file) == 0:
        return []

    try:
        logger.info('Начало маскировки карты')
        with open(file, 'r', encoding='utf-8') as f:
            json_obj = json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []
    except TypeError:
        return []
    except KeyError:
        return []
    except ValueError:
        return []

    logger.info('Начало маскировки карты')
    return json_obj


def get_transaction_sum(transaction: dict = {}) ->  float:
    """ Получение суммы в рублях из входящего словаря транзакции """
    if len(transaction) == 0 or "operationAmount" not in transaction \
            or "amount" not in transaction["operationAmount"] \
            or "currency" not in transaction["operationAmount"]\
            or "code" not in transaction["operationAmount"]["currency"]:
        return 0

    amount = transaction["operationAmount"]["amount"]
    currency = transaction["operationAmount"]["currency"]["code"]

    if currency == "RUB":
        return amount
    else:
        return get_rouble_amount(amount, currency)
