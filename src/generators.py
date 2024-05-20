from typing import Generator, Iterator, List


def filter_by_currency(transactions_dict: List[dict], currency: str) -> Generator:
    """Функция выдает по очереди операции, в которых указана заданная валюта."""
    for operation in transactions_dict:
        if operation["operationAmount"]["currency"]["code"] == currency:
            yield operation


def transaction_descriptions(operations: List[dict]) -> Generator:
    """Возвращает описание каждой операции по очереди"""
    for operation in operations:
        yield operation["description"]


def card_number_generator(start: int, end: int) -> Iterator[str]:
    """Генерирует номера карт в заданном диапазоне"""
    for number in range(start, end + 1):
        card_number_str = str(number)
        card_number = "0" * (16 - len(card_number_str)) + card_number_str
        formatted_card_number = " ".join([card_number[i: i + 4] for i in range(0, 16, 4)])
        yield formatted_card_number
