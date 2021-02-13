import pytest

from ROVMessaging.HashMap import HashMap

@pytest.fixture()
def hashMap():
    return HashMap[str, int]()

def test_can_create_a_hashmap(hashMap):
    assert isinstance(hashMap, HashMap)

def test_adding_an_entry_to_a_hashmap_returns_none_if_the_key_did_not_exist(hashMap):
    key = "Test"
    value = 23

    prevValue = hashMap.put(key, value)

    assert prevValue == None

def test_adding_an_entry_to_a_hashmap_returns_the_previous_value_if_the_key_already_existed(hashMap):
    key = "Meow"
    value = 34

    prevValue = hashMap.put(key, value)

    assert prevValue == None

    value2 = 32
    prevValue2 = hashMap.put(key, value2)

    assert prevValue2 == value

def test_get_a_non_existent_entry_returns_none(hashMap):
    value = hashMap.get("test")

    assert value == None

def test_can_get_an_entry_from_a_hashmap_that_was_stored(hashMap):
    key = "Spicy"
    expectedValue = 12

    hashMap.put(key, expectedValue)

    value = hashMap.get(key)

    assert value == expectedValue

def test_removing_an_entry_returns_none_if_the_key_does_not_exist(hashMap):
    value = hashMap.remove("Spicy")

    assert value == None

def test_removing_an_entry_returns_the_previous_value_if_the_key_exists(hashMap):
    key = "Toasty"
    expectedValue = 45

    hashMap.put(key, expectedValue)
    value = hashMap.remove(key)

    assert value == expectedValue

def test_removing_a_key_removes_the_entry_if_it_exists(hashMap):
    key = "Toasty"
    expectedValue = 45

    hashMap.put(key, expectedValue)
    hashMap.remove(key)

    value = hashMap.get(key)

    assert value == None

def test_hasmap_size_is_zero_if_is_is_empty(hashMap):
    assert hashMap.size() == 0

def test_hasmap_is_correct_size_for_the_number_of_entrys(hashMap):
    hashMap.put("Cool", 23)
    hashMap.put("Super", 61)

    assert hashMap.size() == 2
