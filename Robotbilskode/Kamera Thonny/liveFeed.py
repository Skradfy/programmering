import cv2
import pyaudio
import wave
import threading
import os
from datetime import datetime
from databaseManager import DatabaseManager

class LiveFeed:
    def __init__(self, db_manager: DatabaseManager, video_db_path="database/VideoDB", audio_db_path="database/AudioDB"):
        """Initialiserer live-feed med databasehåndtering og lagringsstier til video/lyd."""
        self.db_manager = db_manager
        self.video_db_path = video_db_path
        self.audio_db_path = audio_db_path
        os.makedirs(self.video_db_path, exist_ok=True)
        os.makedirs(self.audio_db_path, exist_ok=True)
        
        self.video_capture = cv2.VideoCapture(0)  # Standard webcam
        self.frame_width = int(self.video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.frame_height = int(self.video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.fps = 20  # Billeder per sekund til videooptagelse

    def start_audio_recording(self):
        """Starter lydoptagelse og gemmer det i databasen."""
        print("Starter lydoptagelse...")
        audio_thread = threading.Thread(target=self.record_audio)
        audio_thread.start()

    def record_audio(self):
        """Optager lyd fra mikrofonen og gemmer det som en .mp3-fil."""
        p = pyaudio.PyAudio()
        stream = p.open(format=pyaudio.paInt16,
                        channels=1,
                        rate=44100,
                        input=True,
                        frames_per_buffer=1024)

        frames = []
        while True:
            try:
                data = stream.read(1024)
                frames.append(data)
            except KeyboardInterrupt:
                break

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        audio_file_path = os.path.join(self.audio_db_path, f"audio_{timestamp}.wav")
        with wave.open(audio_file_path, 'wb') as wf:
            wf.setnchannels(1)
            wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
            wf.setframerate(44100)
            wf.writeframes(b''.join(frames))
        
        stream.stop_stream()
        stream.close()
        p.terminate()
        print(f"Lyd gemt til {audio_file_path}.")

    def start_video_recording(self):
        """Starter videooptagelse og gemmer det i databasen."""
        print("Starter videooptagelse...")
        video_thread = threading.Thread(target=self.record_video)
        video_thread.start()

    def record_video(self):
        """Optager videobilleder fra webcammet og gemmer det som en .mp4-fil."""
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        video_file_path = os.path.join(self.video_db_path, f"video_{timestamp}.mp4")
        out = cv2.VideoWriter(video_file_path, fourcc, self.fps, (self.frame_width, self.frame_height))

        while True:
            ret, frame = self.video_capture.read()
            if not ret:
                break

            out.write(frame)
            cv2.imshow("Live-feed", frame)

            # Stop, hvis 'q' trykkes
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        out.release()
        self.video_capture.release()
        cv2.destroyAllWindows()
        print(f"Video gemt til {video_file_path}.")

    def run_in_thread(self):
        """Starter både video- og lydoptagelse i separate tråde."""
        print("Starter live-feed...")
        video_thread = threading.Thread(target=self.start_video_recording)
        audio_thread = threading.Thread(target=self.start_audio_recording)

        video_thread.start()
        audio_thread.start()

        video_thread.join()
        audio_thread.join()

    def stop_feed(self):
        """Stopper videooptagelse og live-feed."""
        print("Stopper live-feed...")
        self.video_capture.release()
        cv2.destroyAllWindows()
