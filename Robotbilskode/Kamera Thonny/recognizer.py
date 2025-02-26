import cv2
import numpy as np
from datetime import datetime
from liveFeed import LiveFeed
from databaseManager import DatabaseManager
from faceTrainer import FaceTrainer
from databaseLogger import DatabaseLogger


class Recognizer:
    def __init__(self, db_manager=None, face_db_path="database/FaceDB", log_db_path="logs"):
        """Initialiserer Recognizer med databasehåndtering og ansigtsdatabase."""
        self.face_trainer = FaceTrainer(face_db_path=face_db_path)
        self.db_manager = db_manager or DatabaseManager()  # Hvis ingen databasehåndtering leveres, opret en standard
        self.face_recognizer = cv2.face.LBPHFaceRecognizer_create()
        self.face_trainer.train_recognizer()  # Sørger for, at genkenderen er trænet ved initialisering
        self.logger = DatabaseLogger(log_db_path)  # Logger alt relateret til genkendelse

    def recognize_face(self, frame):
        """Genkender ansigter i et billede."""
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_trainer.face_cascade.detectMultiScale(gray, 1.1, 4)
        
        for (x, y, w, h) in faces:
            face = gray[y:y + h, x:x + w]
            label, confidence = self.face_recognizer.predict(face)
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            if confidence < 100:  # Ansigt genkendt
                label_text = f"Bruger {label}"
                # Logger genkendelsesbegivenheden
                self.logger.save_log(f"Ansigt genkendt: {label_text} kl. {timestamp}")
                print(f"Ansigt genkendt: {label_text} (Sikkerhed: {confidence})")
                self._store_recognition_data(label, timestamp)
            else:
                print("Ukendt ansigt fundet")

    def _store_recognition_data(self, label, timestamp):
        """Gemmer genkendelsesbegivenheden i databasen."""
        try:
            # Gemmer i databasen (kan tilpasses til din specifikke datastruktur)
            recognition_data = {
                'label': label,
                'timestamp': timestamp,
                'event': 'Ansigtsgenkendelse'
            }
            self.db_manager.store_data(recognition_data)  # Forudsat at store_data-metoden findes
        except Exception as e:
            print(f"Fejl ved lagring af genkendelsesdata: {e}")

    def start_recognition(self):
        """Starter genkendelsesprocessen ved brug af live-feed."""
        live_feed = LiveFeed(self.db_manager)  # Forudsat at LiveFeed håndterer både video og lyd
        cap = cv2.VideoCapture(0)  # Optager fra webcammet

        while True:
            ret, frame = cap.read()
            if not ret:
                print("Kunne ikke fange billede")
                break

            self.recognize_face(frame)
            
            # Viser billede med ansigtsgenkendelsesresultat
            cv2.imshow("Ansigtsgenkendelse", frame)
            
            # Stopper ved tryk på 'q'
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()


# Eksempel på brug:
if __name__ == "__main__":
    db_manager = DatabaseManager()  # Forudsat at DatabaseManager er defineret og håndterer databaseforbindelser
    recognizer = Recognizer(db_manager=db_manager)
    recognizer.start_recognition()
