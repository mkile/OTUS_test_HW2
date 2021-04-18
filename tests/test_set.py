import pytest


def test_creation():
    assert isinstance({"1", 2, 3}, set) == True


def test_union(generic_set):
    assert len(generic_set) == len(generic_set.union(generic_set))


@pytest.mark.parametrize('input_value, expected', [(set(range(3)), False),
                                                   (set(range(8)), True)])
def test_issubset(generic_set, input_value, expected):
    assert generic_set.issubset(input_value) == expected


def test_difference(generic_set):
    assert len(generic_set.difference(generic_set)) == 0


@pytest.mark.parametrize('input_value, expected', [(1, {2, 3, 4}),
                                                   (4, {1, 2, 3}),
                                                   pytest.param(5, {1, 2, 3, 4}, marks=pytest.mark.xfail),
                                                   pytest.param('2', {1, 3, 4}, marks=pytest.mark.xfail)])
def test_issubset(generic_set, input_value, expected):
    generic_set.remove(input_value)
    assert generic_set == expected
