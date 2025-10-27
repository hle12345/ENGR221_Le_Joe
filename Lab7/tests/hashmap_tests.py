import unittest
import pytest

import os, sys 

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from myHashMap import MyHashMap

class TestMyHashMapHomework07(unittest.TestCase):
    # i. put()
    def test_put_into_empty(self):
        m = MyHashMap()
        m.put("a", 1)
        self.assertEqual(m.size(), 1)
        self.assertEqual(m.get("a"), 1)

    def test_put_nonempty_without_surpass_load_factor(self):
        m = MyHashMap()
        m.put("a", 1)
        m.put("b", 2)  # still under load factor
        self.assertEqual(m.size(), 2)
        self.assertEqual(m.get("a"), 1)
        self.assertEqual(m.get("b"), 2)

    def test_put_surpass_load_factor(self):
        # Use small initial capacity if your implementation supports it.
        try:
            m = MyHashMap(initial_capacity=4, load_factor=0.75)
        except TypeError:
            # Fallback to default constructor if parameters differ.
            m = MyHashMap()
        # Insert enough keys to exceed load factor; all entries should remain accessible.
        for i in range(8):
            m.put(f"k{i}", i)
        for i in range(8):
            self.assertEqual(m.get(f"k{i}"), i)

    def test_put_existing_key_does_not_duplicate(self):
        m = MyHashMap()
        m.put("a", 1)
        size_before = m.size()
        m.put("a", 99)  # behavior may update or ignore value; must not increase size
        self.assertEqual(m.size(), size_before)

    # ii. replace()
    def test_replace_existing_key(self):
        m = MyHashMap()
        m.put("k", 1)
        m.replace("k", 7)
        self.assertEqual(m.get("k"), 7)

    def test_replace_missing_key(self):
        m = MyHashMap()
        m.replace("missing", 5)
        # Should not create a new entry
        self.assertEqual(m.size(), 0)
        self.assertIsNone(m.get("missing"))

    # iii. remove()
    def test_remove_present_key(self):
        m = MyHashMap()
        m.put("k", 1)
        m.remove("k")
        self.assertIsNone(m.get("k"))
        self.assertEqual(m.size(), 0)

    def test_remove_absent_key(self):
        m = MyHashMap()
        size_before = m.size()
        m.remove("nope")
        self.assertEqual(m.size(), size_before)
          # iv. set()
    def test_set_when_present(self):
        m = MyHashMap()
        m.put("k", 1)
        m.set("k", 42)
        self.assertEqual(m.get("k"), 42)
        self.assertEqual(m.size(), 1)

    def test_set_when_missing(self):
        m = MyHashMap()
        m.set("k", 7)
        self.assertEqual(m.get("k"), 7)
        self.assertEqual(m.size(), 1)

    # v. get()
    def test_get_present(self):
        m = MyHashMap()
        m.put("x", 5)
        self.assertEqual(m.get("x"), 5)

    def test_get_not_present(self):
        m = MyHashMap()
        self.assertIsNone(m.get("ghost"))

    # vi. size()
    def test_size_empty(self):
        m = MyHashMap()
        self.assertEqual(m.size(), 0)

    def test_size_few(self):
        m = MyHashMap()
        m.put("a", 1)
        self.assertEqual(m.size(), 1)

    def test_size_many(self):
        m = MyHashMap()
        for i in range(100):
            m.put(f"k{i}", i)
        self.assertEqual(m.size(), 100)
        