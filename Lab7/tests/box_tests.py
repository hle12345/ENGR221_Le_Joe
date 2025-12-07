import pytest
import os, sys 

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from box import Box
from myHashMap import MyHashMap  # to reset nicknameMap for an empty Box


@pytest.fixture
def populated_box():
    """Return a Box that has been populated from entries.txt."""
    return Box()


@pytest.fixture
def empty_box():
    """Return an empty Box (no entries)."""
    b = Box()
    # Replace the populated nicknameMap with an empty one
    b.nicknameMap = MyHashMap()
    return b


####
# add()
####

@pytest.mark.box
def test_add_new_nickname(empty_box):
    # 1) add() a nickname that does not already exist in the Box
    added = empty_box.add("Sparky", "Pikachu")
    assert added is True
    # The nickname should now be present
    entry = empty_box.findEntryByNickname("Sparky")
    assert entry is not None


@pytest.mark.box
def test_add_existing_nickname(empty_box):
    # 2) add() a nickname that already exists in the Box
    empty_box.add("Sparky", "Pikachu")
    added_again = empty_box.add("Sparky", "Raichu")
    # Should not allow duplicate nicknames
    assert added_again is False


####
# find()
####

@pytest.mark.box
def test_find_existing_entry(populated_box):
    # 1) find() a nickname and species that exists in the Box
    entry = populated_box.find("Sparky", "Pikachu")
    # For an existing nickname and species we expect a non-None Entry object
    assert entry is not None


@pytest.mark.box
def test_find_missing_entry(populated_box):
    # 2) find() a nickname and species that does not exist in the Box
    entry = populated_box.find("NotInBox", "UnknownSpecies")
    assert entry is None


####
# findAllNicknames()
####

@pytest.mark.box
def test_findallnicknames_populated(populated_box):
    # 1) findAllNicknames() of a populated Box
    nicknames = populated_box.findAllNicknames()
    assert isinstance(nicknames, list)
    # There should be at least one nickname in a populated box
    assert len(nicknames) > 0
    # A known nickname from entries.txt should appear
    assert "Sparky" in nicknames


@pytest.mark.box
def test_findallnicknames_empty(empty_box):
    # 2) findAllNicknames() of an empty Box
    nicknames = empty_box.findAllNicknames()
    assert isinstance(nicknames, list)
    assert nicknames == []


####
# findEntryByNickname()
####

@pytest.mark.box
def test_findentrybynickname_exists(populated_box):
    # 1) findEntryByNickname() that exists in the Box
    entry = populated_box.findEntryByNickname("Sparky")
    assert entry is not None


@pytest.mark.box
def test_findentrybynickname_not_exists(populated_box):
    # 2) findEntryByNickname() that does not exist in the Box
    entry = populated_box.findEntryByNickname("NotInBox")
    # The spec says to return an empty list when nickname is not present
    assert entry == []


####
# removeByNickname()
####

@pytest.mark.box
def test_removebynickname_exists(populated_box):
    # 1) removeByNickname() that exists in the Box
    # Ensure the nickname is present first
    assert populated_box.findEntryByNickname("Sparky") is not None
    removed = populated_box.removeByNickname("Sparky")
    assert removed is True
    # After removal, the nickname should not be found
    assert populated_box.findEntryByNickname("Sparky") == []


@pytest.mark.box
def test_removebynickname_not_exists(populated_box):
    # 2) removeByNickname() that does not exist in the Box
    removed = populated_box.removeByNickname("NotInBox")
    assert removed is False


####
# removeEntry()
####

@pytest.mark.box
def test_removeentry_exists(populated_box):
    # 1) removeEntry() of nickname and species that exists in the Box
    entry = populated_box.find("Sparky", "Pikachu")
    assert entry is not None
    removed = populated_box.removeEntry("Sparky", "Pikachu")
    assert removed is True
    # The nickname should no longer be present
    assert populated_box.findEntryByNickname("Sparky") == []


@pytest.mark.box
def test_removeentry_not_exists(populated_box):
    # 2) removeEntry() of nickname and species that is not in the Box
    removed = populated_box.removeEntry("NotInBox", "UnknownSpecies")
    assert removed is False
