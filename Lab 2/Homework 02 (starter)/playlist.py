""""
Author: Joe Le
Filename: playlist.py
Description: Implementation of a playlist as an array with duplicates
"""

from song import Song

class Playlist():
    # The constructor is run every time a new Playlist object is created
    # max_num_songs is the maximum number of songs you can have in the playlist
    def __init__(self, max_num_songs):
        # Stores the songs in the playlist
        # It is initially a list of max_num_songs number of None objects
        self.songs = [None] * max_num_songs
        # The current number of songs in the playlist
        self.num_songs = 0              
        # The maximum number of songs the playlist can have
        self.max_num_songs = max_num_songs

    ###########
    # Methods #
    ###########

    # Return the number of songs in the playlist
    def get_num_songs(self):
        return self.num_songs 
    
    # Return the current songs list
    def get_songs(self):
        return self.songs 
    
    # Return the song at index idx or
    # Return None if idx is outside of bounds
    def get_song_at_idx(self, idx):
        if 0 <= idx and idx < self.num_songs:
            return self.songs[idx]
    
    # Set index idx to the given song
    # Do not change anything if idx is outside of bounds
    def set_song_at_idx(self, idx, song):
        if 0 <= idx and idx < self.num_songs:
            self.songs[idx] = song 

    # Insert a song to the end of the playlist
    def insert_song(self, song):
        self.songs[self.num_songs] = song 

        # Update the length of the playlist
        self.num_songs += 1

    # Return the index of the given song title in the playlist,
    # or return -1 if the song is not in the playlist
    def search_by_title(self, song_title):
        # Only search the indices with songs
        for i in range(self.num_songs):
            # Check the value at the current index 
            if self.songs[i].title == song_title:
                # Return the index
                return i 
            
        # If we got here, we did not find the song so return -1
        return -1
    
    # Delete the first occurrence of the song title in the playlist
    # Returns True if the song was deleted, or False if not
    def delete_by_title(self, song_title):
        # Find the index of the song to delete
        idx = self.search_by_title(song_title)

        # If the song was not found, we cannot delete it
        if idx == -1:
            return False 
        
        # Otherwise, proceed by decrementing the size of the playlist
        self.num_songs -= 1

        # Then shift all the remaining songs in the playlist
        for j in range(idx, self.num_songs):
            self.songs[j] = self.songs[j+1]
        
        # Return True to indicate that the song was deleted
        return True 
    
    # Print all songs in the playlist
    def traverse(self):
        for song in self.songs:
            print(song)

if __name__ == '__main__':
    # You can test your code here
    songs = [Song("Golden", "HUNTR/X"),
             Song("Ordinary", "Alex Warren"),
             Song("What I Want", "Morgan Wallen ft. Tate McRae"),
             Song("Your Idol", "Saja Boys"),
             Song("Soda Pop", "Saja Boys")]
    
    p = Playlist(3)"