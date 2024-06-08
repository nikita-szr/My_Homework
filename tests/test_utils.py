import json
from unittest.mock import ANY, mock_open, patch

from src.utils import json_transactions_data, transaction_amount


def test_json_transactions_data_file_not_found():
    with patch('builtins.open', mock_open()) as mock_file:
        mock_file.side_effect = FileNotFoundError
        result = json_transactions_data('test_file.json')
        assert result == []


def test_json_transactions_data_json_decode_error():
    with patch('builtins.open', mock_open()) as mock_file:
        with patch('json.load') as mock_json_load:
            mock_json_load.side_effect = json.JSONDecodeError('error', '', 0)
            json_transactions_data('test_file.json')
            mock_file.assert_called_once_with('test_file.json', 'r', encoding=ANY)


def test_json_transactions_data_other_exception():
    with patch('builtins.open', mock_open()) as mock_file:
        mock_file.side_effect = Exception('error')
        result = json_transactions_data('test_file.json')
        assert result == []


def test_json_transactions_data_valid_json():
    with patch('builtins.open', mock_open()) as mock_file:
        with patch('json.load') as mock_json_load:
            mock_json_load.return_value = [{'id': 1, 'amount': 100}, {'id': 2, 'amount': 200}]
            json_transactions_data('test_file.json')
            mock_file.assert_called_once_with('test_file.json', 'r', encoding=ANY)


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
