from src.masks import mask_bank_account, mask_card_number
from src.widget import card_or_account_mask, convert_date
from src.processing import filter_dicts, sort_dicts_by_date


masked_card_number = mask_card_number(7000792289606361)
masked_bank_account = mask_bank_account(73654108430135874305)
masked_card_or_account = card_or_account_mask("Maestro 7000792289606361")
converted_date = convert_date("2018-07-11T02:26:18.671407")
filtered_dicts = filter_dicts([
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
])
sorted_dicts = sort_dicts_by_date([
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
])

print(masked_card_number)
print(masked_bank_account)
print(masked_card_or_account)
print(converted_date)
print(filtered_dicts)
print(sorted_dicts)