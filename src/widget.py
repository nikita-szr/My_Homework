from src.masks import mask_bank_account, mask_card_number


def card_or_account_mask(number: str) -> str:
    """Распознает что передано: счёт или карта, и маскирует номер"""
    if "счет" in number.lower():
        account_number = number.split()
        return account_number[0] + " " + mask_bank_account(account_number[1])

    elif "счет" not in number.lower():
        cardnumber = number.split()
        return cardnumber[0] + " " + mask_card_number(cardnumber[1])
    else:
        return "Введённые данные не распознаны"


def convert_date(date: str) -> str:
    """Преобразовывает вид строки с датой операции"""
    full_date = date.split("T")[0]
    year_month_day_split = full_date.split("-")
    converted_date = f"{year_month_day_split[2]}.{year_month_day_split[1]}.{year_month_day_split[0]}"
    return converted_date
