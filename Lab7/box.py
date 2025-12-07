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
        nick = entry.nickname
        if self.nicknameMap.containsKey(nick):
            raise Exception("Nickname already exists")
        self.nicknameMap.put(nick, entry)
 

    """
    Return a single Entry object with the given nickname and species.
    Should not modify the Box itself. 
    Return None if the Entry does not exist in the Box. """
    def find(self, nickname, species):
        try:
            e = self.nicknameMap.get(nickname)
            return (e.nickname == nickname) and (e.species == species)
        except Exception:
            return False


    """ 
    Return a list of nickanames representing all unique 
    nicknames in the Box. Should not modify the Box itself.
    Return an empty list if the Box is empty. """
    def findAllNicknames(self):
        return self.nicknameMap.keys()
 

    """ 
    Return an Entry with the given nickname. Should not modify
    the Box itself. 
    Return an empty list if the nickname is not in the Box. """
    def findEntryByNickname(self, nickname):
        try:
            return self.nicknameMap.get(nickname)
        except Exception:
            return None
 

    """
    Remove the Entry with the given nickname from the Box. 
    Return true if successful, or false otherwise."""
    def removeByNickname(self, nickname):
        removed = self.nicknameMap.remove(nickname)
        return removed is not None
 

    """ 
    Remove the Entry with the given nickname and species. 
    Return true if successful, or false otherwise. """
    def removeEntry(self, nickname, species):
        try:
            e = self.nicknameMap.get(nickname)
        except Exception:
            return False
        if e.species == species:
            self.nicknameMap.remove(nickname)
            return True
        return False
 

if __name__ == '__main__':
    Box()