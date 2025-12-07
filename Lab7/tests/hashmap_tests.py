
# Write your tests here
import pytest
import os, sys 

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from myHashMap import MyHashMap


@pytest.fixture
def empty_map():
    """Return a fresh, empty MyHashMap for each test."""
    return MyHashMap()


@pytest.fixture
def small_map(empty_map):
    """Return a small MyHashMap pre-populated with a couple of entries."""
    empty_map.put("a", 1)
    empty_map.put("b", 2)
    return empty_map


#### 
# put()
####

@pytest.mark.myhashmap
def test_put_into_empty_myhashmap(empty_map):
    # 1) put() into an empty MyHashMap
    added = empty_map.put("k1", 10)
    assert added is True
    assert empty_map.get("k1") == 10
    assert empty_map.size() == 1


@pytest.mark.myhashmap
def test_put_into_nonempty_below_load_factor(small_map):
    # 2) put() into a nonempty MyHashMap and do NOT surpass the load factor
    old_size = small_map.size()
    added = small_map.put("c", 3)
    assert added is True
    assert small_map.get("c") == 3
    assert small_map.size() == old_size + 1


@pytest.mark.myhashmap
def test_put_triggers_resize():
    # 3) put() into a nonempty MyHashMap and surpass the load factor
    m = MyHashMap(load_factor=0.75, initial_capacity=4)
    # Fill up to the load factor
    m.put("k1", 1)
    m.put("k2", 2)
    m.put("k3", 3)
    old_capacity = m.capacity
    # This put should push size/capacity above load_factor and trigger resize()
    m.put("k4", 4)
    assert m.capacity > old_capacity
    # All keys should still be present after resizing
    for i in range(1, 5):
        assert m.get(f"k{i}") == i


@pytest.mark.myhashmap
def test_put_existing_key_returns_false_and_does_not_change_value(small_map):
    # 4) put() a key that already exists in the MyHashMap
    old_size = small_map.size()
    old_value = small_map.get("a")
    added = small_map.put("a", 999)
    assert added is False
    # Existing value and size should be unchanged
    assert small_map.get("a") == old_value
    assert small_map.size() == old_size


####
# replace()
####

@pytest.mark.myhashmap
def test_replace_existing_key(small_map):
    # 1) replace() a key that is already present in the MyHashMap
    replaced = small_map.replace("a", 100)
    assert replaced is True
    assert small_map.get("a") == 100
    # size should not change
    assert small_map.size() == 2


@pytest.mark.myhashmap
def test_replace_missing_key(empty_map):
    # 2) replace() a key that is not present in the MyHashMap
    replaced = empty_map.replace("missing", 5)
    assert replaced is False
    assert empty_map.size() == 0


####
# remove()
####

@pytest.mark.myhashmap
def test_remove_existing_key(small_map):
    # 1) remove() a key that is present in the MyHashMap
    assert small_map.containsKey("a")
    old_size = small_map.size()
    removed = small_map.remove("a")
    assert removed is True
    assert not small_map.containsKey("a")
    assert small_map.size() == old_size - 1


@pytest.mark.myhashmap
def test_remove_missing_key(empty_map):
    # 2) remove() a key that is not present in the MyHashMap
    removed = empty_map.remove("ghost")
    assert removed is False
    assert empty_map.size() == 0


####
# set()
####

@pytest.mark.myhashmap
def test_set_existing_key(small_map):
    # 1) set() a key that is already present in the MyHashMap
    old_size = small_map.size()
    small_map.set("a", 500)
    assert small_map.get("a") == 500
    # size should not change when replacing an existing key
    assert small_map.size() == old_size


@pytest.mark.myhashmap
def test_set_new_key(empty_map):
    # 2) set() a key that is not present in the MyHashMap
    empty_map.set("new", 42)
    assert empty_map.get("new") == 42
    assert empty_map.size() == 1


####
# get()
####

@pytest.mark.myhashmap
def test_get_existing_key(small_map):
    # 1) get() a key that is present in the MyHashMap
    assert small_map.get("a") == 1
    assert small_map.get("b") == 2


@pytest.mark.myhashmap
def test_get_missing_key(empty_map):
    # 2) get() a key that is not present in the MyHashMap
    assert empty_map.get("missing") is None


####
# size()
####

@pytest.mark.myhashmap
def test_size_empty(empty_map):
    # 1) Get the size() of an empty MyHashMap
    assert empty_map.size() == 0


@pytest.mark.myhashmap
def test_size_few_items():
    # 2) Get the size() of a MyHashMap with few items (e.g., 1)
    m = MyHashMap()
    m.put("only", 1)
    assert m.size() == 1


@pytest.mark.myhashmap
def test_size_many_items():
    # 3) Get the size() of a MyHashMap with many items (e.g., 100)
    m = MyHashMap()
    for i in range(100):
        m.put(f"key{i}", i)
    assert m.size() == 100


####
# isEmpty()
####

@pytest.mark.myhashmap
def test_isempty_true_for_empty_map(empty_map):
    # 1) Check whether an empty MyHashMap isEmpty()
    assert empty_map.isEmpty() is True


@pytest.mark.myhashmap
def test_isempty_false_for_nonempty_map():
    # 2) Check whether a nonempty MyHashMap isEmpty()
    m = MyHashMap()
    m.put("x", 1)
    assert m.isEmpty() is False


####
# containsKey()
####

@pytest.mark.myhashmap
def test_containskey_existing(small_map):
    # 1) Check whether a MyHashMap containsKey() that already exists
    assert small_map.containsKey("a")
    assert small_map.containsKey("b")


@pytest.mark.myhashmap
def test_containskey_missing(small_map):
    # 2) Check whether a MyHashMap containsKey() that does not exist
    assert not small_map.containsKey("nope")


####
# keys()
####

@pytest.mark.myhashmap
def test_keys_empty(empty_map):
    # 1) Return keys() for an empty MyHashMap
    keys = empty_map.keys()
    assert isinstance(keys, list)
    assert keys == []


@pytest.mark.myhashmap
def test_keys_nonempty():
    # 2) Return keys() for a nonempty MyHashMap
    m = MyHashMap()
    for k in ("a", "b", "c"):
        m.put(k, k.upper())
    keys = m.keys()
    assert isinstance(keys, list)
    # Order is not guaranteed, so compare as sets
    assert set(keys) == {"a", "b", "c"}
    assert len(keys) == 3
