from typing import Union


def mask_card_number(card_number: int) -> str:
    str_card_number: str = str(card_number)
    masked_card_number = (
        str_card_number[:4]
        + " "
        + str_card_number[4:6]
        + "X" * len(str_card_number[6:8])
        + " "
        + "X" * len(str_card_number[8:11])
        + " "
        + str_card_number[11:15]
    )
    return masked_card_number


def mask_bank_account(account_number: Union[str, int]) -> str:
    """Функция маскирует номер счета оставляя последние 4 цифры"""
    account_number = str(account_number)
    masked_account_number: str = "**" + account_number[-4:]
    return masked_account_number
