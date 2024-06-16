import json
import logging
import os
from typing import Any, Dict, List, Union

import pandas as pd

from src.external_api import currency_conversion

logger = logging.getLogger('utils')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('../logs/utils.log', mode='w')
file_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def transactions_data(path: str) -> list[dict[str, Any]]:
    """Функция принимает на вход путь к файлу, определяет формат
    и возвращает список словарей с данными о финансовых транзакциях"""
    file_path, file_extension = os.path.splitext(path)
    if file_extension == ".json":
        try:
            with open(path, 'r', encoding='utf-8') as json_file:
                json_transactions = json.load(json_file)
                if json_transactions:
                    logger.info(f"json файл перекодирован в список словарей: {transactions_data}")
                    return json_transactions
                else:
                    logger.info(f"в json файле нет словарей: {transactions_data}")
                    return []
        except FileNotFoundError:
            logger.error(f"Файл не найден: {transactions_data}")
            print("Ошибка: Файл не найден.")
            return []
        except json.JSONDecodeError:
            logger.error(f"Файл не является json объектом: {transactions_data}")
            print("Ошибка: Файл не является json объектом.")
            return []
        except Exception as e:
            logger.error(f"Ошибка{e}: {transactions_data}")
            print(f"Ошибка: {e}")
            return []
    elif file_extension == ".csv":
        try:
            df = pd.read_csv(path, sep=';')
            csv_transactions = []
            for index, row in df.iterrows():
                transaction = {
                    "id": row["id"],
                    "state": row["state"],
                    "date": row["date"],
                    "operationAmount": {
                        "amount": row["amount"],
                        "currency": {
                            "name": row["currency_name"],
                            "code": row["currency_code"]
                        }
                    },
                    "description": row["description"],
                    "from": row["from"],
                    "to": row["to"]
                }
                csv_transactions.append(transaction)
            logger.info(f"csv файл перекодирован в список словарей: {transactions_data}")
            return csv_transactions
        except FileNotFoundError:
            logger.error(f"Файл не найден: {transactions_data}")
            print("Ошибка: Файл не найден.")
            return []
        except pd.errors.ParserError:
            logger.error(f"Файл не является csv объектом: {transactions_data}")
            print("Ошибка: Файл не является csv объектом.")
            return []
        except Exception as e:
            logger.error(f"Ошибка{e}: {transactions_data}")
            print(f"Ошибка: {e}")
            return []
    elif file_extension == ".xlsx":
        try:
            df = pd.read_excel(path)
            xlsx_transactions = []
            for index, row in df.iterrows():
                transaction = {
                    "id": row["id"],
                    "state": row["state"],
                    "date": row["date"],
                    "operationAmount": {
                        "amount": row["amount"],
                        "currency": {
                            "name": row["currency_name"],
                            "code": row["currency_code"]
                        }
                    },
                    "description": row["description"],
                    "from": row["from"],
                    "to": row["to"]
                }
                xlsx_transactions.append(transaction)
            logger.info(f"xlsx файл перекодирован в список словарей: {transactions_data}")
            return xlsx_transactions
        except FileNotFoundError:
            logger.error(f"Файл не найден: {transactions_data}")
            print("Ошибка: Файл не найден.")
            return []
        except pd.errors.ParserError:
            logger.error(f"Файл не является xlsx объектом: {transactions_data}")
            print("Ошибка: Файл не является xlsx объектом.")
            return []
        except Exception as e:
            logger.error(f"Ошибка{e}: {transactions_data}")
            print(f"Ошибка: {e}")
            return []
    else:
        logger.error(f"Неподдерживаемый формат файла: {transactions_data}")
        print("Ошибка: Неподдерживаемый формат файла.")
        return []


def transaction_amount(transactions: List[Dict[str, Any]]) -> Union[float, None]:
    """Функция принимает транзакцию и возвращает сумму транзакции в рублях, конвертируя через API запрос"""
    for transaction in transactions:
        if ("operationAmount" in transaction and "currency" in transaction["operationAmount"]
                and "code" in transaction["operationAmount"]["currency"]):
            currency_code = transaction["operationAmount"]["currency"]["code"]
            if currency_code == "RUB":
                amount = float(transaction["operationAmount"]["amount"])
                logger.info(f"Определена сумма транзакции в рублях: {transactions_data}")
                return amount
            else:
                amount_: float | None = currency_conversion(currency_code, "RUB",
                                                            float(transaction["operationAmount"]["amount"]))
                logger.info(f"Сумма транзакции конвертирована в рубли: {transactions_data}")
                return amount_
        else:
            logger.error(f"Некорректный формат данных транзакции: {transactions_data}")
            print("Ошибка: Некорректный формат данных транзакции.")
            result = None
    return result
