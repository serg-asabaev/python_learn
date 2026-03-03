import json
import os

import requests
from dotenv import load_dotenv


def get_rouble_amount(amount: float, currency: str) -> float:
    """Конвертация суммы в валюте в рубли"""

    url = f"https://api.apilayer.com/currency_data/convert?to=RUB&from={currency}&amount={amount}"

    load_dotenv()
    api_key = os.getenv("API_KEY")

    # payload = {}
    headers = {"apikey": api_key}
    response = requests.get(url, headers=headers)

    return response.json()['result']
