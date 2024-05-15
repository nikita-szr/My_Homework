import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions, transactions


def testing_filter_by_currency_usd():
    usd_transactions = list(filter_by_currency(transactions, "USD"))
    assert usd_transactions[0]["id"] == 939719570
    assert usd_transactions[1]["id"] == 142264268
    assert usd_transactions[2]["id"] == 895315941


def testing_filter_by_currency_rub():
    rub_transactions = list(filter_by_currency(transactions, "RUB"))
    assert rub_transactions[0]["id"] == 873106923
    assert rub_transactions[1]["id"] == 594226727


@pytest.fixture
def operations():
    return [
        {"description": "Перевод организации"},
        {"description": "Перевод со счета на счет"},
        {"description": "Перевод с карты на карту"},
    ]


def testing_transaction_descriptions(operations):
    descriptions = transaction_descriptions(operations)
    assert next(descriptions) == "Перевод организации"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод с карты на карту"


@pytest.mark.parametrize(
    "start, end, expected",
    [
        (1, 4, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003", "0000 0000 0000 0004"]),
        (10, 12, ["0000 0000 0000 0010", "0000 0000 0000 0011", "0000 0000 0000 0012"]),
        (100, 102, ["0000 0000 0000 0100", "0000 0000 0000 0101", "0000 0000 0000 0102"]),
    ],
)
def testing_card_number_generator(start, end, expected):
    generator = card_number_generator(start, end)
    result = list(generator)
    assert result == expected
