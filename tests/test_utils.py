import json
from unittest.mock import ANY, mock_open, patch

import pandas as pd

from src.utils import transaction_amount, transactions_data


def test_transactions_data_file_not_found():
    with patch('builtins.open', mock_open()) as mock_file:
        mock_file.side_effect = FileNotFoundError
        result = transactions_data('test_file.json')
        assert result == []


def test_transactions_data_json_decode_error():
    with patch('builtins.open', mock_open()) as mock_file:
        with patch('json.load') as mock_json_load:
            mock_json_load.side_effect = json.JSONDecodeError('error', '', 0)
            transactions_data('test_file.json')
            mock_file.assert_called_once_with('test_file.json', 'r', encoding=ANY)


def test_transactions_data_other_exception():
    with patch('builtins.open', mock_open()) as mock_file:
        mock_file.side_effect = Exception('error')
        result = transactions_data('test_file.json')
        assert result == []


def test_transactions_data_valid_json():
    with patch('builtins.open', mock_open()) as mock_file:
        with patch('json.load') as mock_json_load:
            mock_json_load.return_value = [{'id': 1, 'amount': 100}, {'id': 2, 'amount': 200}]
            transactions_data('test_file.json')
            mock_file.assert_called_once_with('test_file.json', 'r', encoding=ANY)


def test_csv_transactions_data_file_not_found():
    with patch('pandas.read_csv') as mock_read_csv:
        mock_read_csv.side_effect = FileNotFoundError
        result = transactions_data('test_file.csv')
        assert result == []


def test_csv_transactions_data_invalid_csv():
    with patch('pandas.read_csv') as mock_read_csv:
        mock_read_csv.side_effect = pd.errors.ParserError
        result = transactions_data('test_file.csv')
        assert result == []


def test_csv_transactions_data_valid_csv():
    with patch('pandas.read_csv') as mock_read_csv:
        mock_read_csv.return_value = pd.DataFrame({
            "id": [1, 2],
            "state": ["EXECUTED", "CANCELED"],
            "date": ["2023-09-05", "2020-12-06"],
            "amount": ["16210", "29740"],
            "currency_name": ["Sol", "Peso"],
            "currency_code": ["PEN", "COP"],
            "from": ["Счет 58803664561298323391", "Discover 3172601889670065"],
            "to": ["Счет 39745660563456619397", "Discover 0720428384694643"],
            "description": ["Перевод организации", "Перевод с карты на карту"]
        })
        result = transactions_data('test_file.csv')
        assert result == [
            {
                "id": 1,
                "state": "EXECUTED",
                "date": "2023-09-05",
                "operationAmount": {
                    "amount": "16210",
                    "currency": {
                        "name": "Sol",
                        "code": "PEN"
                    }
                },
                "description": "Перевод организации",
                "from": "Счет 58803664561298323391",
                "to": "Счет 39745660563456619397"
            },
            {
                "id": 2,
                "state": "CANCELED",
                "date": "2020-12-06",
                "operationAmount": {
                    "amount": "29740",
                    "currency": {
                        "name": "Peso",
                        "code": "COP"
                    }
                },
                "description": "Перевод с карты на карту",
                "from": "Discover 3172601889670065",
                "to": "Discover 0720428384694643"
            }
        ]


def test_xlsx_transactions_data_file_not_found():
    with patch('pandas.read_excel') as mock_read_excel:
        mock_read_excel.side_effect = FileNotFoundError
        result = transactions_data('test_file.xlsx')
        assert result == []


def test_xlsx_transactions_data_invalid_xlsx():
    with patch('pandas.read_excel') as mock_read_excel:
        mock_read_excel.side_effect = pd.errors.ParserError
        result = transactions_data('test_file.xlsx')
        assert result == []


def test_xlsx_transactions_data_valid_xlsx():
    with patch('pandas.read_excel') as mock_read_excel:
        mock_read_excel.return_value = pd.DataFrame({
            "id": [1, 2],
            "state": ["EXECUTED", "CANCELED"],
            "date": ["2023-09-05", "2020-12-06"],
            "amount": ["16210", "29740"],
            "currency_name": ["Sol", "Peso"],
            "currency_code": ["PEN", "COP"],
            "from": ["Счет 58803664561298323391", "Discover 3172601889670065"],
            "to": ["Счет 39745660563456619397", "Discover 0720428384694643"],
            "description": ["Перевод организации", "Перевод с карты на карту"]
        })
        result = transactions_data('test_file.xlsx')
        assert result == [
            {
                "id": 1,
                "state": "EXECUTED",
                "date": "2023-09-05",
                "operationAmount": {
                    "amount": "16210",
                    "currency": {
                        "name": "Sol",
                        "code": "PEN"
                    }
                },
                "description": "Перевод организации",
                "from": "Счет 58803664561298323391",
                "to": "Счет 39745660563456619397"
            },
            {
                "id": 2,
                "state": "CANCELED",
                "date": "2020-12-06",
                "operationAmount": {
                    "amount": "29740",
                    "currency": {
                        "name": "Peso",
                        "code": "COP"
                    }
                },
                "description": "Перевод с карты на карту",
                "from": "Discover 3172601889670065",
                "to": "Discover 0720428384694643"
            }
        ]


def test_transaction_in_rub():
    with patch('src.external_api.currency_conversion') as mock_conversion:
        mock_conversion.side_effect = AssertionError("Should not be called")
        transactions = [{"operationAmount": {"currency": {"code": "RUB"}, "amount": "100"}}]
        result = transaction_amount(transactions)
        assert result == 100.0


def test_transaction_not_in_rub():
    with patch('src.external_api.currency_conversion') as mock_conversion:
        mock_conversion.return_value = 120.0
        transactions = [{"operationAmount": {"currency": {"code": "USD"}, "amount": "100"}}]
        result = transaction_amount(transactions)
        assert result is None


def test_multiple_transactions():
    with patch('src.external_api.currency_conversion') as mock_conversion:
        mock_conversion.side_effect = [120.0, 150.0]
        transactions = [
            {"operationAmount": {"currency": {"code": "USD"}, "amount": "100"}},
            {"operationAmount": {"currency": {"code": "EUR"}, "amount": "120"}}
        ]
        result = transaction_amount(transactions)
        assert result is None
