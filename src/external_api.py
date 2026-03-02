import os
import json
import requests
from dotenv import load_dotenv


def get_rouble_amount(amount: float, currency: str) -> float:
    """Конвертация суммы в валюте в рубли"""

    url = f"https://api.apilayer.com/currency_data/convert?to=RUB&from={currency}&amount={amount}"

    load_dotenv()
    api_key = os.getenv("API_KEY")

    # payload = {}
    headers = {"apikey": api_key}

    try:
        response = requests.get(url, headers=headers)
        result = json.loads(response.text)['result']
    except Exception as e:
        result = 0

    return result
