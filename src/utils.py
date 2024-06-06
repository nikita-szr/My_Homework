import json
from src.external_api import currency_conversion
def json_transactions_data(path):
    """Функция принимает на вход json файл и возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(path, 'r', encoding='utf-8') as file:
            transactions = json.load(file)
            if transactions:
                return transactions
            else:
                return []
    except FileNotFoundError:
        print(f"Ошибка: Файл не найден.")
        return []
    except json.JSONDecodeError:
        print(f"Ошибка: Файл не является json объектом.")
        return []
    except Exception as e:
        print(f"Ошибка: {e}")
        return []


def transaction_amount(transactions):
    """Функция принимает транзакцию и возвращает сумму транзакции в рублях, конвертируя через API запрос"""
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == "RUB":
            amount = float(transaction["operationAmount"]["amount"])
            return amount
        else:
            currency = transaction["operationAmount"]["currency"]["code"]
            amount = currency_conversion(currency, "RUB", float(transaction["operationAmount"]["amount"]))
            return amount
