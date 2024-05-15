import pytest

from src.processing import filter_dicts, sort_dicts_by_date


@pytest.fixture
def testing_filter_dicts():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "PENDING", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "EXECUTED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELLED", "date": "2018-10-14T08:21:33.419441"},
    ]


def test_filter_dicts(testing_filter_dicts):
    assert filter_dicts(testing_filter_dicts, "EXECUTED") == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 594226727, "state": "EXECUTED", "date": "2018-09-12T21:27:25.241689"},
    ]
    assert filter_dicts(testing_filter_dicts, "PENDING") == [
        {"id": 939719570, "state": "PENDING", "date": "2018-06-30T02:08:58.425572"}
    ]
    assert filter_dicts(testing_filter_dicts, "CANCELLED") == [
        {"id": 615064591, "state": "CANCELLED", "date": "2018-10-14T08:21:33.419441"}
    ]
    assert filter_dicts(testing_filter_dicts, "INVALID_STATE") == []


@pytest.mark.parametrize(
    "dicts, filter, expecting_order",
    [
        ([], True, []),
        ([{"date": "2022-01-01"}], True, [{"date": "2022-01-01"}]),
        (
            [{"date": "2022-01-03"}, {"date": "2022-01-01"}, {"date": "2022-01-02"}],
            True,
            [{"date": "2022-01-03"}, {"date": "2022-01-02"}, {"date": "2022-01-01"}],
        ),
        (
            [{"date": "2022-01-03"}, {"date": "2022-01-01"}, {"date": "2022-01-02"}],
            False,
            [{"date": "2022-01-01"}, {"date": "2022-01-02"}, {"date": "2022-01-03"}],
        ),
    ],
)
def test_sort_dicts_by_date(dicts, filter, expecting_order):
    assert sort_dicts_by_date(dicts, filter) == expecting_order