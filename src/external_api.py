import os
import json
import requests
from dotenv import load_dotenv

def get_rouble_amount(amount: float, currency: str) -> float:
    """ Конвертация суммы в валюте в рубли """

    url = f"https://api.apilayer.com/currency_data/convert?to=RUB&from={currency}&amount={amount}"

    payload = {}
    headers = {
    }

    load_dotenv()
    api_key = os.getenv('API_KEY')
    headers['apikey'] = api_key

    response = requests.request("GET", url, headers=headers, data=payload)
    result = json.loads(response.text)['result']

    return result
