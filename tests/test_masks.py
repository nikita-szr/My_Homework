import pytest

from src.masks import mask_bank_account, mask_card_number


@pytest.fixture
def testing_card_numbers():
    return [1234567812345678, 1234, "12345678123456781234567812345678", 7000792289606361]


def test_mask_card_number(testing_card_numbers):
    assert mask_card_number(testing_card_numbers[0]) == "1234 56XX XXXX 5678"
    assert mask_card_number(testing_card_numbers[1]) == "Неверный номер карты"
    assert mask_card_number(testing_card_numbers[2]) == "Неверный номер карты"
    assert mask_card_number(testing_card_numbers[3]) == "7000 79XX XXXX 6361"


@pytest.fixture
def testing_bank_accounts():
    return [48126790351872493601, 69540218372591084732, 82107364928504617395]


def test_mask_bank_account(testing_bank_accounts):
    assert mask_bank_account(testing_bank_accounts[0]) == "**3601"
    assert mask_bank_account(testing_bank_accounts[1]) == "**4732"
    assert mask_bank_account(testing_bank_accounts[2]) == "**7395"
