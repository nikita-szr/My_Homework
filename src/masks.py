from typing import Union
import logging


logger = logging.getLogger('masks')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('../logs/masks.log', mode='w')
file_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def mask_card_number(card_number: Union[str, int]) -> str:
    """Маскирует номер карты"""
    str_card_number: str = str(card_number)
    if len(str_card_number) == 16:
        masked_card_number = (
            str_card_number[:4]
            + " "
            + str_card_number[4:6]
            + "X" * len(str_card_number[6:8])
            + " "
            + "X" * len(str_card_number[8:12])
            + " "
            + str_card_number[12:16]
        )
        logger.info(f"Номер карты замаскирован: {masked_card_number}")
        return masked_card_number
    logger.error(f"Неверный номер карты: {card_number}")
    return "Неверный номер карты"


def mask_bank_account(account_number: Union[str, int]) -> str:
    """Функция маскирует номер счета оставляя последние 4 цифры"""
    account_number = str(account_number)
    if len(account_number) > 19:
        masked_account_number: str = "**" + account_number[-4:]
        logger.info(f"Номер счёта замаскирован: {masked_account_number}")
        return masked_account_number
    logger.error(f'Неверный номер счёта: {account_number}')
    return "Неверный номер счёта"
