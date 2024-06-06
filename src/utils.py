import os
import json
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

