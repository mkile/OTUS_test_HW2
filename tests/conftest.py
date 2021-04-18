import pytest


@pytest.fixture
def generic_dict():
    generic_dict = {1: 1, 2: 2, '3': '3'}
    yield generic_dict
    del generic_dict


@pytest.fixture
def generic_set():
    generic_set = {1, 2, 3, 4}
    yield generic_set
    del generic_set


@pytest.fixture
def generic_list():
    generic_list = [1, 2, 3, 4, '5']
    yield generic_list
    del generic_list


@pytest.fixture(scope='module')
def generic_list_module():
    generic_list_module = [1, 2]
    yield generic_list_module
    del generic_list_module
