"""
WRITE YOUR PROGRAM HEADER HERE

Adapted from UCSD CSE12
"""

class MyHashMap:
    def __init__(self, load_factor=0.75,
                       initial_capacity=16):
        self.load_factor = load_factor
        self.capacity = initial_capacity
        self._size = 0                 # <-- internal counter
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
               # Raises an Exception when key is None.
        if key is None:
            raise Exception("Key cannot be None")

        # Find the bucket for this key
        index = keyHash % self.capacity
        bucket = self.buckets[index]

        # If the key already exists, do nothing and return False
        for entry in bucket:
            if entry.getKey() == key:
                return False

        # Check load factor using the current number of entries
        current_size = self.get_size()
        if (current_size + 1) / self.capacity > self.load_factor:
            # Resize, then recompute index and bucket
            self.resize()
            index = hash(key) % self.capacity
            bucket = self.buckets[index]

        # Add new key–value pair
        bucket.append(MyHashMap.MyHashMapEntry(key, value))
        self._size += 1               
        return True



    
    def replace(self, key, newValue):
        """Replace the value stored for key with newValue.
        Returns True if key existed and was replaced, False otherwise.
        Raises Exception if key is None.
        """
               # Raise an exception if the key is None
        if key is None:
            raise Exception("Key cannot be None")

        index = hash(key) % self.capacity
        bucket = self.buckets[index]

        for entry in bucket:
            if entry.getKey() == key:
                entry.setValue(newValue)
                return True

        # Key was not found
        return False

    """
    Remove the entry corresponding to the given key.
    Return true if an entry for the given key was removed.
    Raise an exception if the key is None. """
    def remove(self, key):
                # Raise an exception if the key is None
        if key is None:
            raise Exception("Key cannot be None")

        index = hash(key) % self.capacity
        bucket = self.buckets[index]

        for i, entry in enumerate(bucket):
            if entry.getKey() == key:
                # Remove this entry from the bucket
                del bucket[i]
                self._size -= 1  
                return True
        # Key not found
        return False



    """
    Adds the key, value pair to the MyHashMap if it is not present.
    Otherwise, replace the existing value for that key with the given value.
    Raise an exception if the key is None. """
    def set(self, key, value):
                # Raise an exception if the key is None
        if key is None:
            raise Exception("Key cannot be None")

        # If key already present, just replace its value
        if self.containsKey(key):
            self.replace(key, value)
        else:
            # Otherwise, insert as a new key
            self.put(key, value)



    """
    Return the value of the specified key. If the key is not in the
    MyHashMap, return None.
    Raise an exception if the key is None. """
    def get(self, key):
               # Raise an exception if the key is None
        if key is None:
            raise Exception("Key cannot be None")

        index = hash(key) % self.capacity
        bucket = self.buckets[index]

        for entry in bucket:
            if entry.getKey() == key:
                return entry.getValue()

        # Key not found
        return None


    """
    Return the number of key, value pairs in this MyHashMap. """
    def get_size(self):
        """Return the number of key, value pairs (Homework 07 version)."""
        return self.size()      # <- call the size() method

    
    def size(self):
        """Compatibility method: used by the Lab 7 tests."""
        return self._size



    """
    Return true if the MyHashMap contains no elements, and 
    false otherwise. """
    def isEmpty(self):
        """Return True if map has no entries, False otherwise."""
                # Map is empty if it has zero key–value pairs
        return self.get_size() == 0



    """
    Return true if the specified key is in this MyHashMap. 
    Raise an exception if the key is None. """
    def containsKey(self, key):
                # Raise an exception if the key is None
        if key is None:
            raise Exception("Key cannot be None")

        index = hash(key) % self.capacity
        bucket = self.buckets[index]

        for entry in bucket:
            if entry.getKey() == key:
                return True

        return False



        """
    Return a list containing the keys of this MyHashMap. 
    If it is empty, return an empty list. """
    def keys(self):
               # Collect all keys from all buckets
        key_list = []
        for bucket in self.buckets:
            for entry in bucket:
                key_list.append(entry.getKey())
        return key_list

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
