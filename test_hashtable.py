import pytest
from hashtable import HashTable, BLANK


def test_should_create_hashtable():
    assert HashTable(capacity=100) is not None


def test_should_report_capacity():
    assert len(HashTable(capacity=100)) == 100


def test_should_create_empty_value_slots():
    assert HashTable(capacity=3).values == [BLANK, BLANK, BLANK]


def test_should_insert_key_value_pairs():
    hash_table = HashTable(capacity=50)
    hash_table["cola"] = "Coke"
    hash_table[2.71] = 42
    hash_table[False] = True

    assert "Coke" in hash_table.values
    assert 42 in hash_table.values
    assert True in hash_table.values

    assert len(hash_table) == 50


@pytest.mark.skip
def test_should_not_shrink_when_removing_elements():
    pass


def test_should_not_contain_none_value_when_created():
    assert None not in HashTable(capacity=5000).values


def test_should_insert_none_value():
    hash_table = HashTable(capacity=10)
    hash_table["key"] = None
    assert None in hash_table.values
