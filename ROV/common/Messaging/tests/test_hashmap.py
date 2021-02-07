import pytest

from HashMap import HashMap

@pytest.fixture
def hashMap():
    return HashMap()

def test_can_create_a_hashmap(hashMap):
    assert isinstance(hashMap, HashMap)

def test_can_add_an_element_to_a_hashmap():
    assert False

def test_adding_an_element_to_a_hashmap_returns_the_previous_value_if_the_key_already_existed():
    assert False

def test_adding_an_element_to_a_hashmap_returns_none_if_the_key_did_not_exist():
    assert False

def test_can_get_an_element_to_a_hashmap():
    assert False

def test_get_a_non_existent_element_returns_none():
    assert False

def test_can_remove_an_element_to_a_hashmap():
    assert False

def test_removing_an_element_returns_the_previous_value_if_the_key_exists():
    assert False

def test_removing_an_element_returns_none_if_the_key_does_not_exist():
    assert False

def test_hasmap_size_is_zero_if_is_is_empty():
    assert False

def test_hasmap_is_correct_for_the_number_of_elements():
    assert False
