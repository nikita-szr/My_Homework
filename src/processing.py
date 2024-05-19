from typing import List

operations = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


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
