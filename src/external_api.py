from dotenv import load_dotenv
import os
import requests

load_dotenv()
exchange_rates_data_API = os.getenv("API_KEY_CONVERTATION")
def currency_conversion(from_currency, to_currency, amount):
    """Функция конвертирует сумму из одной валюты в другую с использованием API обмена валют"""
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to_currency}&from={from_currency}&amount={amount}"
    headers = {
        "apikey": exchange_rates_data_API
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data['result']
    else:
        print(f"Ошибка: {response.status_code}, {response.text}")
        return None