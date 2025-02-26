import os
import cv2
import numpy as np
from datetime import datetime

class FaceTrainer:
    def __init__(self, face_db_path="database/FaceDB", model_path="database/face_recognizer.yml"):
        """Initialiserer FaceTrainer med stier til databasen og modellen."""
        self.face_db_path = face_db_path
        self.model_path = model_path
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        self.recognizer = cv2.face.LBPHFaceRecognizer_create()

    def initialize_user(self, user_name):
        """Initialiserer brugerens mappe i FaceDB til lagring af optagede ansigter."""
        self.user_name = user_name.strip()
        self.user_folder_path = os.path.join(self.face_db_path, self.user_name)
        os.makedirs(self.user_folder_path, exist_ok=True)
        print(f"Brugermappe oprettet for {self.user_name}.")

    def train_recognizer(self):
        """Træner ansigtsgenkendelsesmodellen ved hjælp af alle billeder i FaceDB."""
        images = []
        labels = []
        label_map = {}

        # Indsamler alle ansigter og deres tilsvarende etiketter
        for idx, user_folder in enumerate(os.listdir(self.face_db_path)):
            user_path = os.path.join(self.face_db_path, user_folder)
            if os.path.isdir(user_path):
                label_map[idx] = user_folder
                for image_name in os.listdir(user_path):
                    image_path = os.path.join(user_path, image_name)
                    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
                    images.append(image)
                    labels.append(idx)

        # Træner modellen med de indsamlede billeder og etiketter
        self.recognizer.train(images, np.array(labels))
        self.recognizer.save(self.model_path)  # Gemmer den trænede model
        print(f"Ansigtsgenkendelsesmodel trænet og gemt til {self.model_path}.")

    def run_face_registration(self):
        """Optager og gemmer ansigter til træningsformål."""
        cap = cv2.VideoCapture(0)  # Åbner webcammet
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Konverterer til gråtone for ansigtsdetektion
            faces = self.face_cascade.detectMultiScale(gray, 1.1, 4)  # Finder ansigter i billedet

            # For hvert detekteret ansigt gemmes billedet med et tidsstempel
            for (x, y, w, h) in faces:
                face = gray[y:y + h, x:x + w]
                timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                face_filename = f"{self.user_name}_{timestamp}.jpg"
                face_path = os.path.join(self.user_folder_path, face_filename)
                cv2.imwrite(face_path, face)
                print(f"Ansigt gemt: {face_filename}")

            # Viser live video-feed med rektangler til ansigtsdetektion
            cv2.imshow("Ansigtsregistrering", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):  # Tryk 'q' for at stoppe registreringen
                break

        cap.release()
        cv2.destroyAllWindows()
