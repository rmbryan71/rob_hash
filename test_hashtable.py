import pytest
from hashtable import HashTable, BLANK


@pytest.fixture
def hash_table():
    sample_data = HashTable(capacity=500)
    sample_data["cola"] = "Coke"
    sample_data[2.71] = 42
    sample_data[False] = True
    return sample_data


def test_should_find_value_by_key(hash_table):
    assert hash_table["cola"] == "Coke"
    assert hash_table[2.71] == 42
    assert hash_table[False] is True


def test_should_raise_error_on_missing_key():
    hash_table = HashTable(capacity=100)
    with pytest.raises(KeyError) as exception_info:
        hash_table["missing_key"]
    assert exception_info.value.args[0] == "missing_key"
# I don't know why line 23 is flagged for having no effect


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


def test_should_find_key(hash_table):
    assert "cola" in hash_table


def test_should_not_find_key(hash_table):
    assert "missing_key" not in hash_table


def test_should_get_value(hash_table):
    assert hash_table.get("cola") == "Coke"


def test_should_get_none_when_missing_key(hash_table):
    assert hash_table.get("missing_key") is None


def test_should_get_default_value_when_missing_key(hash_table):
    assert hash_table.get("missing_key", "default") == "default"


def test_should_get_value_with_default(hash_table):
    assert hash_table.get("cola", "default") == "Coke"
