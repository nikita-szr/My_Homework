import json
from typing import Any, Dict, List, Union

from src.external_api import currency_conversion


def json_transactions_data(path: str) -> List[Dict[str, Any]]:
    """Функция принимает на вход json файл и возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(path, 'r', encoding='utf-8') as file:
            transactions = json.load(file)
            if transactions:
                return transactions
            else:
                return []
    except FileNotFoundError:
        print("Ошибка: Файл не найден.")
        return []
    except json.JSONDecodeError:
        print("Ошибка: Файл не является json объектом.")
        return []
    except Exception as e:
        print(f"Ошибка: {e}")
        return []


def transaction_amount(transactions: List[Dict[str, Any]]) -> Union[float, None]:
    """Функция принимает транзакцию и возвращает сумму транзакции в рублях, конвертируя через API запрос"""
    for transaction in transactions:
        if ("operationAmount" in transaction and "currency" in transaction["operationAmount"]
                and "code" in transaction["operationAmount"]["currency"]):
            currency_code = transaction["operationAmount"]["currency"]["code"]
            if currency_code == "RUB":
                amount = float(transaction["operationAmount"]["amount"])
                return amount
            else:
                amount_: float | None = currency_conversion(currency_code, "RUB",
                                                            float(transaction["operationAmount"]["amount"]))
                return amount_
        else:
            print("Ошибка: Некорректный формат данных транзакции.")
            result = None
    return result
