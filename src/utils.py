import json

from mypy.types_utils import UnionType
from src.external_api import get_rouble_amount


def get_operations_list(file: str = '') -> list[dict]:
    """ Получение json-обьекта из указанного файла """

    if len(file) == 0:
        return []

    try:
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

    return json_obj


def get_transaction_sum(transaction: dict = {}) -> UnionType(int, float):
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
