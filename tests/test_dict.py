import pytest


def test_creation():
    assert isinstance({"1": 2}, dict) == True


def test_clear(generic_dict):
    generic_dict.clear()
    assert len(generic_dict) == 0


@pytest.mark.parametrize('input_value, expected', [(1, 1),
                                                   (2, 2),
                                                   ('3', '3'),
                                                   pytest.param('4', '4', marks=pytest.mark.xfail)])
def test_getvalue(generic_dict, input_value, expected):
    assert generic_dict.get(input_value) == expected


def test_values(generic_dict):
    assert list(generic_dict.values()) == [1, 2, '3']


def test_pop(generic_dict):
    assert generic_dict.pop(1) == 1 & (len(generic_dict) == 2)
