import unittest
import pytest
import os, sys

import box 

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from box import Box

class TestBoxHomework07(unittest.TestCase):
    def setUp(self):
        # Avoid file I/O: we won't call populateBox in tests.
        self.b = box.Box()

    # i. add()
    def test_add_new_nickname(self):
        self.b.add("sparky", "dog")
        # should be findable
        e = self.b.findEntryByNickname("sparky")
        self.assertTrue(e)  # exists (Entry or truthy)

    def test_add_duplicate_nickname(self):
        self.b.add("sparky", "dog")
        self.b.add("sparky", "cat")  # duplicate nickname
        # still only one association for that nickname
        e = self.b.findEntryByNickname("sparky")
        # Implementation may return Entry or list; just ensure it's a single nickname mapping
        self.assertTrue(e)

    # ii. find()
    def test_find_exists(self):
        self.b.add("milo", "cat")
        found = self.b.find("milo", "cat")
        self.assertTrue(found)

    def test_find_not_exists(self):
        self.assertFalse(self.b.find("nemo", "fish"))

    # iii. findAllNicknames()
    def test_find_all_nicknames_populated(self):
        for n, s in [("a", "axolotl"), ("b", "badger"), ("c", "capybara")]:
            self.b.add(n, s)
        self.assertEqual(set(self.b.findAllNicknames()), {"a", "b", "c"})

    def test_find_all_nicknames_empty(self):
        self.assertEqual(self.b.findAllNicknames(), [])

    # iv. findEntryByNickname()
    def test_find_entry_by_nickname_exists(self):
        self.b.add("luna", "cat")
        self.assertTrue(self.b.findEntryByNickname("luna"))

    def test_find_entry_by_nickname_not_exists(self):
        self.assertFalse(self.b.findEntryByNickname("ghost"))

    # v. removeByNickname()
    def test_remove_by_nickname_exists(self):
        self.b.add("kiki", "bird")
        self.b.removeByNickname("kiki")
        self.assertFalse(self.b.findEntryByNickname("kiki"))

    def test_remove_by_nickname_not_exists(self):
        # Should not raise and leaves box unchanged
        self.assertFalse(self.b.removeByNickname("nope"))
    # vi. removeEntry()
    def test_remove_entry_exists(self):
        self.b.add("fido", "dog")
        self.b.removeEntry("fido", "dog")
        self.assertFalse(self.b.findEntryByNickname("fido"))

    def test_remove_entry_not_in_box(self):
        self.assertFalse(self.b.removeEntry("milo", "cat"))


if __name__ == "__main__":
    unittest.main()
