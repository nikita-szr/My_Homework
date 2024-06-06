from unittest.mock import mock_open, patch
from src.utils import json_transactions_data, transaction_amount
import json
from src.external_api import currency_conversion

def test_json_transactions_data_file_not_found():
    with patch('builtins.open', mock_open()) as mock_file:
        mock_file.side_effect = FileNotFoundError
        result = json_transactions_data('test_file.json')
        assert result == []

def test_json_transactions_data_json_decode_error():
    with patch('builtins.open', mock_open()) as mock_file:
        with patch('json.load') as mock_json_load:
            mock_json_load.side_effect = json.JSONDecodeError('error', '', 0)
            result = json_transactions_data('test_file.json')
            assert result == []

def test_json_transactions_data_other_exception():
    with patch('builtins.open', mock_open()) as mock_file:
        mock_file.side_effect = Exception('error')
        result = json_transactions_data('test_file.json')
        assert result == []

def test_json_transactions_data_valid_json():
    with patch('builtins.open', mock_open()) as mock_file:
        with patch('json.load') as mock_json_load:
            mock_json_load.return_value = [{'id': 1, 'amount': 100}, {'id': 2, 'amount': 200}]
            result = json_transactions_data('test_file.json')
            assert result == [{'id': 1, 'amount': 100}, {'id': 2, 'amount': 200}]


