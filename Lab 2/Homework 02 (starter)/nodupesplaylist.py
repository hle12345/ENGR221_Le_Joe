""""
Author: Joe Le
Filename: noduplesplaylist.py
"""

class NoDupesPlaylist: 
    def __init__(self,initial_songs):
        cap = len(initial_songs)
        if cap < 1:
            cap = 1
        self.songs = [None] * cap
        self.num_songs = 0
        # Insert each unique-by-title song (preserve first occurrance order)
        i = 0
        n = len(initial_songs)
        while i < n:
            song = initial_songs[i]
            if self.search_by_title(song.title) == -1:
                self._insert_raw(song)
            i =+ 1

#helpers
    def capacity (self):
        return len (self.songs)
    
    def _grow (self):
        #Double capacity (or go to 1 from 0), copy existing items
        new_cap = self.capacity() * 2 if self.capacity() > 0 else 1
        new_arr = [None] * new_cap
        i = 0
        while i < self.num_songs:
            new_arr[i] = self.songs[i]
            i += 1
        self.songs = new_arr    

    def _insert_raw(self,song):
        if self.num_songs == self.capacity():
            self._grow()
        self.songs[self.num_songs] = song
        self.num_song += 1

# required API
    def search_by_title(self,title):
        """Return index of first song whose title matches, else -1:"""
        i = 0 
        while i < self.num_songs:
            s = self.songs [i] # s is never None for i < num_songs
            if s.title == title:
                return i 
            i += 1
            return -1        
    def insert_song(self, song):
        """ Insert inly if no existing song has the same title"""
        if self.search_by_title(song.title) != -1:
            return
        self._insert_raw(song)

    def delete_by_title(self, title):
        """Delete exactly ONE song by title. Return True if deleted, else False"""
        idx = self.search_by_title(title)
        if idx == -1:
            return False
        
        # shift elements left from idx+1..num_song-1
        write = idx
        read = idx + 1
        while read <self.num_songs:
            self.songs[write] = self.songs[read]
            write += 1
            read += 1
        # clear last used slot and shrink logical length    
        self.songs[self.num_songs - 1] = None
        self.num_songs -= 1
        return True
    
    def traverse (self):
        """Print each song as 'Title - Artist'."""
        i = 0 
        while i < self.num_songs:
            s = self.songs [i]
            print(f"{s.title} - {s.artist}")
            i += 1

# legacy alias to tolerate the old typo in tests
NoDuplesPlaylist = NoDupesPlaylist


