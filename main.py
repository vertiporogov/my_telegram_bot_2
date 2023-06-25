import requests
import json

import os

# CURRENCY_RATES_FILE = "currency_rates.json"
API_KEY = os.getenv('EXCHANGE_RATE_API_KEY')
# print(API_KEY)

def main():
    while True:
        currency = input('Какая валюта интересует?').upper()
        if currency not in ('USD', 'EUR'):
            print('Только USD или  EUR')
            continue

        rate = get_currency_rate(currency)
        print(f'Курс {currency} к рублю: {rate}')
        break


def get_currency_rate(base: str) -> float:
    """Получает курс валюты от API и возвращает его в виде float"""

    url = "https://api.apilayer.com/exchangerates_data/latest"


    response = requests.get(url, headers={'apikey': API_KEY}, params={'base': base})
    # print(response.json)

if __name__ == '__main__':
    main()
# print(get_currency_rate('RUB'))