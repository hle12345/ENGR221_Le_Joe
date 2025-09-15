""""
Author: Joe Le
Filename: playlist.py
Description: Implementation of a playlist as an array with duplicates
"""

from song import Song

class Playlist:
    # The constructor is run every time a new Playlist object is created
    def __init__(self, initial_songs):
        n = len (initial_songs)
        self.songs = [None] * n
        i = 0
        while i < n:
            self.songs[i] = initial_songs[i]
            i += 1
        self.num_songs = n 
        self.max_num_songs = n

    def _capacity (self):
        return len(self.songs)

    def _grow(self):
        new_cap = 1 if self._capacity() == 0 else self.capacity() * 2 
        new_arr = [None] * new_cap
        i = 0
        while i < self.num_songs:
            new_arr[i] = self.song[i]
            i += 1
            self.songs = new_arr
            self.max_num_songs = new_cap
    
    def _ensure_space(self):
        if self.num_songs >= self._capacity():
            self._grow()


    ###########
    # Methods #
    ###########
    def _grow_if_needed(self):
        if self.num_songs == self.max_num_songs:
            new_cap = 1 if self.max_num_songs == 0 else self.max_num_songs * 2
            new_arr = [None] * new_cap
            i = 0
            while i < self.num_songs:
                new_arr[i] = self.songs[i]
                i += 1
                self.songs = new_arr
                self.max_num_songs = new_cap

    def insert_song(self, song):
        # Limitation 2: auto-extend when full (no append/+)
        #Grow BEFORE writing into the next slot.
        self._ensure_space()
        self.songs[self.num_songs] = song
        self.num_songs += 1
    
   
    def get_song_at_idx(self, idx):
        if 0 <= idx < self.num_songs:
            return self.songs[idx]
        return None


    # Delete the first occurrence of the song title in the playlist
    # Returns True if the song was deleted, or False if not
    def delete_by_title(self, title):
        # Limitation 3: delete ALL matches; return how many were deleted
        #Compact in place and COUNT deletions.
        old_n = self.num_songs
        read = 0 
        write = 0
        deleted = 0
        while read < old_n:
            if self.songs[read].title == title:
               deleted += 1
            else:
               self.songs[write] = self.songs[read]
               write += 1
            read += 1
        
        #IMPORTANT: shrink underlying list so p.songs compares equal in tests. 
        new_n = old_n - deleted 
        shrunk = [None] * new_n
        i = 0 
        while i < new_n:
            shrunk[i] = self.songs[i]
            i += 1 
        self.songs = shrunk
        self.num_songs = new_n
        self.max_num_songs = new_n
        return deleted
             
