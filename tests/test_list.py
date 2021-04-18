import pytest


def test_creation():
    assert isinstance([1, 2, '3'], list) == True


def test_len(generic_list):
    assert len(generic_list) == 5


def test_extend(generic_list):
    base_len = len(generic_list)
    generic_list.extend(generic_list)
    assert len(generic_list) == base_len * 2


@pytest.mark.parametrize('input_value, expected', [(1, 0),
                                                   (2, 1),
                                                   (4, 3),
                                                   pytest.param('4', 3, marks=pytest.mark.xfail)])
def test_index(generic_list, input_value, expected):
    assert generic_list.index(input_value) == expected


def test_append(generic_list_module):
    generic_list_module.append(1)
    assert len(generic_list_module) == 3


def test_count(generic_list_module):
    assert generic_list_module.count(1) == 2
