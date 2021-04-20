import pytest


def test_creation():
    assert isinstance("create test string", str) == True


def test_sum():
    assert "test string" + " 1" == "test string 1"


def test_mul():
    assert "1" * 5 == "11111"


@pytest.mark.parametrize('input_value, expected', [('11', True),
                                                   ('46.36', False),
                                                   ('12,66', False),
                                                   ('Text', False)])
def test_isdigit(input_value, expected):
    assert input_value.isdigit() == expected


@pytest.mark.parametrize('input_value, expected', [('1234', '4'),
                                                   ('46.36', '6'),
                                                   ('12,65', '5'),
                                                   pytest.param('Text', 'B', marks=pytest.mark.xfail)])
def test_endswith(input_value, expected):
    assert input_value.endswith(expected) == True

