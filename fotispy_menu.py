from fotispy_song import song_1, song_2, song_3
from fotispy_playlist import Playlist

class Menu:
    
    def __init__(self):
        self.playlist = Playlist()
    
    def display_menu(self):
        print("\n--- Playlist Menu ---")
        print("1. Add Song to Playlist")
        print("2. View Playlist")
        print("3. Remove Song from Playlist")
        print("4. Play All Songs")
        print("5. Shuffle and Play")
        print("6. Exit")
    
    def choose_song(self):
        print("\nAvailable Songs:")
        print("1. Drum a Funk")
        print("2. Street View")
        print("3. Bar Code")
        choice = input("Choose a song number: ")
        if choice == '1':
            return song_1
        elif choice == '2':
            return song_2
        elif choice == '3':
            return song_3
        else:
            print("Invalid option, please try again.")
            return None

    def view_playlist(self):
        if not self.playlist.songs:
            print("\nThe playlist is currently empty.")
        else:
            print("\nCurrent Playlist:")
            for idx, song in enumerate(self.playlist.songs, 1):
                print(f"{idx}. {song}")
    
    def run(self):
        while True:
            self.display_menu()
            choice = input("Choose an option: ")
            
            if choice == '1':
                song = self.choose_song()
                if song:
                    self.playlist.add_song(song)
            
            elif choice == '2':
                self.view_playlist()
            
            elif choice == '3':
                song = self.choose_song()
                if song:
                    self.playlist.remove_song(song)
            
            elif choice == '4':
                self.playlist.play_all()
            
            elif choice == '5':
                self.playlist.shuffle()

            elif choice == '6':
                print("Exiting the playlist menu.")
                break
            
            else:
                print("Invalid option, please try again.")
