import requests


def get_rouble_amount(amount: float, currency: str) -> float:
    """ Конвертация суммы в валюте в рубли """

    data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    course = float(data['Valute'][currency]['Value'])
    result = float(amount) * course

    return result
