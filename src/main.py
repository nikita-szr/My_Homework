from src.masks import mask_bank_account, mask_card_number

masked_card_number = mask_card_number(7000792289606361)
masked_bank_account = mask_bank_account(73654108430135874305)


print(masked_card_number)
print(masked_bank_account)
