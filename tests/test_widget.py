import pytest

from src.widget import card_or_account_mask, convert_date


@pytest.fixture
def testing_card_or_account_mask():
    return [
        ("счет 1234567812345678", "Неверный номер счёта"),
        ("счет 12345678123456781234567812345678", "**5678"),
        ("карта 1234567812345678", "карта 1234 56XX XXXX 5678"),
        ("карта 1234567812345678", "карта 1234 56XX XXXX 5678"),
        ("некорректные данные", "Неверный номер карты"),
    ]


def test_card_or_account_mask(testing_card_or_account_mask):
    for numbers, expecting_mask in testing_card_or_account_mask:
        assert card_or_account_mask(numbers) == expecting_mask


@pytest.mark.parametrize(
    "input_date, expected_output",
    [
        ("2022-05-01T00:00:00", "01.05.2022"),
        ("2022-12-31T00:00:00", "31.12.2022"),
        ("2023-02-30T00:00:00", "30.02.2023"),
        ("2023-06-15T00:00:00", "15.06.2023"),
    ],
)
def test_convert_date(input_date, expected_output):
    assert convert_date(input_date) == expected_output
