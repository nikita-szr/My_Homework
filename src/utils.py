import json
import logging
from typing import Any, Dict, List, Union

from src.external_api import currency_conversion

logger = logging.getLogger('utils')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('../logs/utils.log', mode='w')
file_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def json_transactions_data(path: str) -> List[Dict[str, Any]]:
    """Функция принимает на вход json файл и возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(path, 'r', encoding='utf-8') as file:
            transactions = json.load(file)
            if transactions:
                logger.info(f"json файл перекодирован в список словарей: {json_transactions_data}")
                return transactions
            else:
                logger.info(f"в json файле нет словарей: {json_transactions_data}")
                return []
    except FileNotFoundError:
        logger.error(f"Файл не найден: {json_transactions_data}")
        print("Ошибка: Файл не найден.")
        return []
    except json.JSONDecodeError:
        logger.error(f"Файл не является json объектом: {json_transactions_data}")
        print("Ошибка: Файл не является json объектом.")
        return []
    except Exception as e:
        logger.error(f"Ошибка{e}: {json_transactions_data}")
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
                logger.info(f"Определена сумма транзакции в рублях: {json_transactions_data}")
                return amount
            else:
                amount_: float | None = currency_conversion(currency_code, "RUB",
                                                            float(transaction["operationAmount"]["amount"]))
                logger.info(f"Сумма транзакции конвертирована в рубли: {json_transactions_data}")
                return amount_
        else:
            logger.error(f"Некорректный формат данных транзакции: {json_transactions_data}")
            print("Ошибка: Некорректный формат данных транзакции.")
            result = None
    return result
