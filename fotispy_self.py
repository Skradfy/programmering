import simpleaudio as sa
import random

class Song:
    
    def __init__(self, title, name, length, file_path):
        self.title = title
        self.name = name
        self.length = length
        self.file_path = file_path
        
        
    def __str__(self):
        return f"{self.title} - {self.name} ({self.length} seconds)"
    
    def play(self):
        wave_obj = sa.WaveObject.from_wave_file(self.file_path)
        play_obj = wave_obj.play()
        play_obj.wait_done()
        
class Playlist:
        
    def __init__(self):
        self.songs = []
        
    def add_song(self, song):
        self.songs.append(song)
        print("Tilføjede {song.title} til listen")
        print("Nuværende liste:")
        for index, song in enumerate(self.songs, 1):
            print(f"{index}. {song}")
            
    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
            print(f"Fjernede {song.title} fra listen")
        else:
            print("sang ikke fundet på listen.")
        print("Opdateret liste:")
        for index, song in enumerate(self.songs, 1):
            print(f"{index}. {song}")
            
    def play_all(self):
        if not self.songs:
            print("Listen er tom!")
            return
            
        for song in self.songs:
            print("Afspiller: {song}")
            song.play()
            
        
    def shuffle(self):
        if not  self.songs:
            print("Listen er tom!")
            return
            
        random.shuffle(self.songs)
        print("listen er blevet blandet. Afspiller nu:")
            
        for song in self.songs:
            print("Afspiller: {song}")
            song.play()
        
    def play_playlist(self, loop=False):
        while True:
            self.play_all()
            if not loop:
                break
                
            choice = input("Vil du spille listen igen? (y/n):")
            if choice.lower() != "y":
                break
                
        print("Listen er færdig")
            
class Menu:
    def __init__(self):
        self.playlist = Playlist()
    
    def display_menu(self):
        print("\n --- Playlist Menu ---")
        print("1. Tilføj sang til listen")
        print("2.Fjern sang fra listen")
        print("3. Afspil udvalgte sange")
        print("4. Shuffle og afspil")
        print("5. Exit")
        
    def choose_song(self):
        print("\n Tilgængelige sange:")
        print("1. Drum a Funk")
        print("2. Street View")
        print(" Bar Code")
        choice = input("Vælg et sangnummer: ")
        if choice == "1":
            return song_1
        elif choice == "2":
            return song_2
        elif choice == "3":
            return song_3
        else:
            print("kan ikek lade sig gøre, prøv igen")
            return None
    
    def run(self):
        while True:
            self.display_menu()
            choice = input("Vælg en mulighed: ")
            
            if choice == "1":
                song = self.choose_song()
                if song:
                    self.playlist.add_song(song)
            
            elif choice == "2":
                song = self.choose_song()
                if song:
                    self.playlist.remove_song(song)
            
            elif choice == "3":
                self.playlist.play_playlist(loop=False)
            
            elif choice == "4":
                self.playlist.shuffle()
            
            elif choice == "5":
                print("Går ud af programmet.")
                break
            
            else:
                print("Valg ikke muligt, prøv igen")

song_1 = Song("Drum a Funk", "Ben Darling", "0:04", "C:\\Users\\rolle\\OneDrive\\Musik\\drum_a_funk.wav")
song_2 = Song("Street View", "The Hoist Trio", "0:47", "C:\\Users\\rolle\\OneDrive\\Musik\\street_view.wav")
song_3 = Song("Bar Code", "Maniacs", "0:38", "C:\\Users\\rolle\\OneDrive\\Musik\\bar_code.wav")


menu = Menu()
menu.run()
            
            
        