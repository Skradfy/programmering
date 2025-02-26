import simpleaudio as sa

class Song:
    
    def __init__(self, title, artist, length, file_path):
        self.title = title
        self.artist = artist
        self.length = length
        self.file_path = file_path
        
    def __str__(self):
        return f"Title: {self.title}, Artist: {self.artist}, Length: {self.length}"
    
    def play(self):
        audio = sa.WaveObject.from_wave_file(self.file_path)
        play_obj = audio.play()
        play_obj.wait_done()

# Define songs
song_1 = Song("Drum a Funk", "Ben Darling", "0:04", "C:\\Users\\rolle\\OneDrive\\Musik\\drum_a_funk.wav")
song_2 = Song("Street View", "The Hoist Trio", "0:47", "C:\\Users\\rolle\\OneDrive\\Musik\\street_view.wav")
song_3 = Song("Bar Code", "Maniacs", "0:38", "C:\\Users\\rolle\\OneDrive\\Musik\\bar_code.wav")
