from src.masks import mask_bank_account, mask_card_number
from src.widget import card_or_account_mask, convert_date

masked_card_number = mask_card_number(7000792289606361)
masked_bank_account = mask_bank_account(73654108430135874305)
masked_card_or_account = card_or_account_mask("Maestro 7000792289606361")
converted_date = convert_date("2018-07-11T02:26:18.671407")

print(masked_card_number)
print(masked_bank_account)
print(masked_card_or_account)
print(converted_date)
