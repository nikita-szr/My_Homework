from src.decorators import log
from src.generators import (card_number_generator, filter_by_currency,
                            transaction_descriptions)
from src.masks import mask_bank_account, mask_card_number
from src.processing import filter_dicts, operations, sort_dicts_by_date
from src.widget import card_or_account_mask, convert_date
from src.utils import json_transactions_data, transaction_amount

transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]

masked_card_number = mask_card_number(7000792289606361)
masked_bank_account = mask_bank_account(73654108430135874305)
masked_card_or_account = card_or_account_mask("Maestro 7000792289606361")
converted_date = convert_date("2018-07-11T02:26:18.671407")
filtered_dicts = filter_dicts(operations)
sorted_dicts = sort_dicts_by_date(operations)
usd_transactions = filter_by_currency(transactions, "USD")
descriptions = transaction_descriptions(transactions)
card_number = card_number_generator(1, 5)

print(masked_card_number)
print(masked_bank_account)
print(masked_card_or_account)
print(converted_date)
print(filtered_dicts)
print(sorted_dicts)
print(next(usd_transactions)["id"])
print(next(descriptions))
print(next(card_number))


@log(filename="mylog.txt")
def my_function(x, y):
    return x + y


my_function(1, 2)


transactions_dict = json_transactions_data(r"../data/operations.json")
transaction_amount_rub = transaction_amount(transactions_dict)
print(transactions_dict)
print(transaction_amount_rub)