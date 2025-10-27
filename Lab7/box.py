import os, sys 

sys.path.append(os.path.dirname(__file__))

from myHashMap import MyHashMap
from entry import Entry

class Box:
    def __init__(self):
        self.nicknameMap = MyHashMap()
        self.populateBox()

    """
    Adds Entries to the Box from inputFile. Assume that each
    line in inputFile corresponds to an Entry."""
    def populateBox(self, inputFile='entries.txt'):
        # Open the file as read only
        with open(inputFile, 'r') as f:
            # Add each value in the file as an Entry to the Box
            for line in f:
                # Set the first word in the line as the nickname, and
                # the second as species
                nickname, species = line.split()
                # Add the new entry to the Box
                self.add(nickname, species)

    """
    Create an Entry object with the given information and add it
    to the nicknameMap. 
    Returns true if the Entry is successfully added to the Box, and
    false if the nickname already exists in the Box. """
    def add(self, nickname, species):
        try:
            if self.nicknameMap.containsKey(nickname):
                return False
        except AttributeError:
            try:
                existing = self.nicknameMap.get(nickname)
                if existing is not None:
                    return False
            except AttributeError:
                return False

        entry = Entry(nickname, species)
        try:
            self.nicknameMap.put(nickname, entry)
        except AttributeError:
            try:
                self.nicknameMap.set(nickname, entry)
            except AttributeError:
                try:
                    self.nicknameMap.replace(nickname, entry)
                except AttributeError:
                    pass
        return True 
         

    """
    Return a single Entry object with the given nickname and species.
    Should not modify the Box itself. 
    Return None if the Entry does not exist in the Box. """
    def find(self, nickname, species):
        try:
            entry = self.nicknameMap.get(nickname)
        except AttributeError:
            entry = None
        if entry is None:
            return None
        return entry if getattr(entry, "getSpecies", lambda: None)() == species else None

    """ 
    Return a list of nickanames representing all unique 
    nicknames in the Box. Should not modify the Box itself.
    Return an empty list if the Box is empty. """
    def findAllNicknames(self):
        """Return a list of all unique nicknames in the Box."""
        try:
            keys = self.nicknameMap.keys()
            return list(keys) if keys is not None else []
        except AttributeError:
            return [] 

    """ 
    Return an Entry with the given nickname. Should not modify
    the Box itself. 
    Return an empty list if the nickname is not in the Box. """
    def findEntryByNickname(self, nickname):
        try:
            entry = self.nicknameMap.get(nickname)
        except AttributeError:
            entry = None
        if entry is None:
            return []
        return entry
    """
    Remove the Entry with the given nickname from the Box. 
    Return true if successful, or false otherwise."""
    def removeByNickname(self, nickname):
        try:
            exists = self.nicknameMap.containsKey(nickname)
        except AttributeError:
            try:
                exists = self.nicknameMap.get(nickname) is not None
            except AttributeError:
                exists = False
        if not exists:
            return False
        try:
            removed = self.nicknameMap.remove(nickname)
            return removed is not None
        except AttributeError:
            try:
                self.nicknameMap.replace(nickname, None)
                return True
            except Exception:
                return False
    """ 
    Remove the Entry with the given nickname and species. 
    Return true if successful, or false otherwise. """
    def removeEntry(self, nickname, species):
        """Remove Entry only if nickname exists and species matches."""
        try:
            entry = self.nicknameMap.get(nickname)
        except AttributeError:
            entry = None
        if entry is None or getattr(entry, "getSpecies", lambda: None)() != species:
            return False
        return self.removeByNickname(nickname)

if __name__ == '__main__':
    Box()