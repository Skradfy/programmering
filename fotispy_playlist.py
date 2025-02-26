import random
import time

class Playlist:
    
    def __init__(self):
        self.songs = []
    
    def add_song(self, song):
        self.songs.append(song)
        print(f"Added {song.title} to the playlist.")
    
    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
            print(f"Removed {song.title} from the playlist.")
        else:
            print("Song not found in the playlist.")
    
    def play_all(self, loop=False):
        if not self.songs:
            print("The playlist is empty!")
            return
        
        print("Playing all songs in the playlist:")
        while True:
            for song in self.songs:
                print(f"Playing: {song}")
                song.play()
                time.sleep(1)
            if not loop:
                break
            print("Repeating playlist...")

    def shuffle(self):
        if not self.songs:
            print("The playlist is empty!")
            return
        
        random.shuffle(self.songs)
        print("Shuffled playlist:")
        self.play_all()

    def play_playlist(self, loop=False):
        print("Playing the entire playlist:")
        self.play_all(loop=loop)
