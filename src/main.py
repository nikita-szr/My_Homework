from src.utils import transactions_data, dict_of_category, transactions_by_description
from src.processing import sort_dicts_by_date
from src.widget import convert_date
from src.masks import mask_bank_account, mask_card_number
from src.widget import card_or_account_mask

def main():
    while True:
        print(f'''Привет! Добро пожаловать в программу работы с банковскими транзакциями. 
        Выберите необходимый пункт меню:
        1. Получить информацию о транзакциях из JSON-файла
        2. Получить информацию о транзакциях из CSV-файла
        3. Получить информацию о транзакциях из XLSX-файла''')
        user_file_choice = input().strip()
        if user_file_choice == "1":
            print("Для обработки выбран JSON-файл.")
            transactions = transactions_data(r"../data/operations.json")
            break
        elif user_file_choice == "2":
            print("Для обработки выбран CSV-файл.")
            transactions = transactions_data(r"../data/transactions.csv")
            break
        elif user_file_choice == "3":
            print("Для обработки выбран XLSX-файл.")
            transactions = transactions_data(r"../data/transactions_excel.xlsx")
            break
        else:
            print(f'Ответ {user_file_choice} не распознан')
    while True:
        user_state_choice = input(
            'Введите статус, по которому необходимо выполнить фильтрацию. '
            'Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING: ').upper()
        if user_state_choice in dict_of_category["state"]:
            sorted_transactions = transactions_by_description(transactions, user_state_choice)
            print(f"Операции отфильтрованы по статусу {user_state_choice}")
            break
        else:
            print(f'Статус операции {user_state_choice} недоступен.')
    while True:
        user_date_choice = input('Отсортировать операции по дате? Да/Нет: ')
        if user_date_choice == 'да':
            user_date_choice_bool = input("Отсортировать по возрастанию или по убыванию?: ").lower()
            if user_date_choice_bool == "по возрастанию":
                sorted_transactions_by_date = sort_dicts_by_date(sorted_transactions, sorting_filter=False)
                break
            elif user_date_choice_bool == "по убыванию":
                sorted_transactions_by_date = sort_dicts_by_date(sorted_transactions)
                break
            else:
                print(f'Ответ {user_date_choice_bool} не распознан')
        elif user_date_choice == "нет":
            sorted_transactions_by_date = sorted_transactions
            break
        else:
            print(f'Ответ {user_date_choice} не распознан')
    while True:
        user_ruble_transactions_choice = input("Выводить только рублевые транзакции? Да/Нет: ").lower()
        if user_ruble_transactions_choice == "да":
            ruble_transactions = []
            for transaction in sorted_transactions_by_date:
                if transaction["operationAmount"]["currency"]["code"] == "RUB":
                    ruble_transactions.append(transaction)
            break
        elif user_ruble_transactions_choice == "нет":
            ruble_transactions = sorted_transactions_by_date
            break
        else:
            print(f'Ответ {user_ruble_transactions_choice} не распознан')
    while True:
        user_filter_by_description = (
            input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет: ").lower())
        if user_filter_by_description == "да":
            user_description = input("Введите слово для фильтрации транзакций").lower()
            filtered_by_description = []
            for transaction in ruble_transactions:
                if user_description in transaction["description"]:
                    filtered_by_description.append(transaction)
            break
        elif user_filter_by_description == "нет":
            filtered_by_description = ruble_transactions
            break
        else:
            print(f'Ответ {user_filter_by_description} не распознан')
    if filtered_by_description:
        print(f'Распечатываю итоговый список транзакций...')
        print(f'Всего банковских операций в выборке: {len(filtered_by_description)}')
        for transaction in filtered_by_description:
            date = convert_date(transaction["date"])
            description = transaction["description"]
            card_or_account_from = ""
            if "from" in transaction:
                card_or_account_from = card_or_account_mask(transaction["from"])
            card_or_account_to = card_or_account_mask(transaction["to"])
            amount = transaction["operationAmount"]["amount"]
            code = transaction["operationAmount"]["currency"]["code"]
            print(f'''{date} {description}
            
{card_or_account_from} -> {card_or_account_to}
Сумма: {amount} {code}''')
    else:
        print(f'Программа: Не найдено ни одной транзакции, подходящей под ваши условия фильтрации')


if __name__ == "__main__":
    main()
