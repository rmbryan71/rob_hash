import pytest
from hashtable import HashTable


def test_should_create_hashtable():
    assert HashTable(capacity=100) is not None


def test_should_report_capacity():
    assert len(HashTable(capacity=100)) == 100


def test_should_create_empty_value_slots():
    assert HashTable(capacity=3).values == [None, None, None]


def test_should_insert_key_value_pairs():
    hash_table = HashTable(capacity=5)
    hash_table["cola"] = "Coke"
    hash_table[2.71] = 42
    hash_table[False] = True

    assert "Coke" in hash_table.values
    assert 42 in hash_table.values
    assert True in hash_table.values

    assert len(hash_table) == 5


@pytest.mark.skip
def test_should_not_shrink_when_removing_elements():
    pass
