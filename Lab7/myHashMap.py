"""
name: Joe Le
ENGR221_Lab7,

Adapted from UCSD CSE12
"""

class MyHashMap:
    def __init__(self, load_factor=0.75,
                       initial_capacity=16):
        self.load_factor = load_factor 
        self.capacity = initial_capacity 
        self.size = 0
        self.buckets = [[] for _ in range(self.capacity)]

    """
    Resizes the self.buckets array when the load_factor is reached. """
    def resize(self):
        # Double the number of buckets
        self.capacity *= 2 
        # Make a copy of the current contents in the buckets
        old_buckets = self.buckets 
        # Create a new set of buckets that's twice as big as the old one
        self.buckets = [[] for _ in range(self.capacity)]
        # Add each key, value pair already in the MyHashMap to the new buckets
        for bucket in old_buckets:
            if bucket != []:
                for entry in bucket:
                    self.put(entry.getKey(), entry.getValue())

    """
    Adds the specified key, value pair to the MyHashMap if 
    the key is not already in the MyHashMap. If adding a new key would
    surpass the load_factor, resize the MyHashMap before adding the key.
    Return true if successfully added to the MyHashMap.
    Raise an exception if the key is None. """
    def put(self, key, value):
        keyHash = hash(key)
        if key is None:
            raise ValueError("key cannot be None")

        # if key already exists, don't insert
        if self.containsKey(key):
            return False

        # compute future size from buckets (avoid relying on self.size,
        # which can be off during/after resize because resize() calls put())
        current_count = sum(len(b) for b in self.buckets)
        if (current_count + 1) / self.capacity >= self.load_factor:
            self.resize()

        # keep and use this line ONLY in put(), as requested
        index = keyHash % self.capacity

        self.buckets[index].append(MyHashMap.MyHashMapEntry(key, value))
        # we won't rely on self.size for correctness, but incrementing is harmless
        self.size += 1
        return True

    """
    Replaces the value that maps to the given key if it is present.
    Input: key is the key whose mapped value is being replaced.
           newValue is the value to replace the existing value with.
    Return true if the key was in this MyHashMap and replaced successfully.
    Raise an exception if the key is None. """
    def replace(self, key, newValue):
        if key is None:
            raise ValueError("key cannot be None")

        index = hash(key) % self.capacity
        for entry in self.buckets[index]:
            if entry.getKey() == key:
                entry.setValue(newValue)
                return True
        return False
    """
    Remove the entry corresponding to the given key.
    Return true if an entry for the given key was removed.
    Raise an exception if the key is None. """
    def remove(self, key):
        if key is None:
            raise ValueError("key cannot be None")

        index = hash(key) % self.capacity
        bucket = self.buckets[index]
        for i, entry in enumerate(bucket):
            if entry.getKey() == key:
                del bucket[i]
                self.size -= 1
                return True
        return False

    """
    Adds the key, value pair to the MyHashMap if it is not present.
    Otherwise, replace the existing value for that key with the given value.
    Raise an exception if the key is None. """
    def set(self, key, value):
        if key is None:
            raise ValueError("key cannot be None")

        index = hash(key) % self.capacity
        # update if present
        for entry in self.buckets[index]:
            if entry.getKey() == key:
                entry.setValue(value)
                return False  # updated existing 

    """
    Return the value of the specified key. If the key is not in the
    MyHashMap, return None.
    Raise an exception if the key is None. """
    def get(self, key):
        if key is None:
            raise ValueError("key cannot be None")

        index = hash(key) % self.capacity
        for entry in self.buckets[index]:
            if entry.getKey() == key:
                return entry.getValue()
        return None
    """
    Return the number of key, value pairs in this MyHashMap. """
    def size(self):
        return sum(len(b) for b in self.buckets) 

    """
    Return true if the MyHashMap contains no elements, and 
    false otherwise. """
    def isEmpty(self):
        return self.size() == 0
 

    """
    Return true if the specified key is in this MyHashMap. 
    Raise an exception if the key is None. """
    def containsKey(self, key):
        if key is None:
            raise ValueError("key cannot be None")

        index = hash(key) % self.capacity
        for entry in self.buckets[index]:
            if entry.getKey() == key:
                return True
        return False 

    """
    Return a list containing the keys of this MyHashMap. 
    If it is empty, return an empty list. """
    def keys(self):
        output = []
        for bucket in self.buckets:
            for entry in bucket:
                output.append(entry.getKey())
        return output 

    class MyHashMapEntry:
        def __init__(self, key, value):
            self.key = key 
            self.value = value 

        def getKey(self):
            return self.key 
        
        def getValue(self):
            return self.value 
        
        def setValue(self, new_value):
            self.value = new_value 

if __name__ == "__main__":
    pass