from typing import List


def filter_dicts(dicts: List[dict], state: str = "EXECUTED") -> List[dict]:
    """Возвращает список словарей отфильтрованный по ключу "state" """
    filtered_dicts = []
    for dict in dicts:
        if dict.get("state") == state:
            filtered_dicts.append(dict)
    return filtered_dicts


def sort_dicts_by_date(dicts: List[dict], sorting_filter: bool = True) -> List[dict]:
    """Функция сортирует список словарей с датами операций по календарному порядку"""
    sorted_dicts = sorted(dicts, key=lambda x: x["date"], reverse=sorting_filter)
    return sorted_dicts
