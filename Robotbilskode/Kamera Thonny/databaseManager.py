import os
import sqlite3
from datetime import datetime

class DatabaseManager:
    def __init__(self, db_path="database"):
        """Initialiserer DatabaseManager med en angivet database-sti."""
        self.db_path = db_path
        os.makedirs(self.db_path, exist_ok=True)
        
        # Stier til specifikke databaser (Man kan oprette flere databaser til forskellige datatyper)
        self.face_db_path = os.path.join(self.db_path, "FaceDB")
        self.num_db_path = os.path.join(self.db_path, "PhoneNumberDB")
        self.alarm_db_path = os.path.join(self.db_path, "AlarmDB")
        self.video_db_path = os.path.join(self.db_path, "VideoDB")
        self.audio_db_path = os.path.join(self.db_path, "AudioDB")
        
        # Initialiserer SQLite-databaserne
        self._initialize_databases()

    def _initialize_databases(self):
        """Initialiserer de nødvendige databaser."""
        # Eksempel på en SQLite-database til telefonnumre (Man kan udvide dette til andre typer)
        self.num_db = self._initialize_phone_number_db()
        self.alarm_db = self._initialize_alarm_db()

    def _initialize_phone_number_db(self):
        """Initialiserer telefonnummer-databasen."""
        num_db = sqlite3.connect(os.path.join(self.db_path, "PhoneNumberDB.db"))
        cursor = num_db.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                phone_number TEXT
            )
        ''')
        num_db.commit()
        return num_db

    def _initialize_alarm_db(self):
        """Initialiserer alarm-databasen."""
        alarm_db = sqlite3.connect(os.path.join(self.db_path, "AlarmDB.db"))
        cursor = alarm_db.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS alarms (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT,
                action TEXT,
                details TEXT
            )
        ''')
        alarm_db.commit()
        return alarm_db

    def save_face_data(self, user_name, face_image_path):
        """Gemmer et ansigtsbillede i databasen."""
        face_folder_path = os.path.join(self.face_db_path, user_name)
        os.makedirs(face_folder_path, exist_ok=True)
        face_data = os.path.basename(face_image_path)
        destination_path = os.path.join(face_folder_path, face_data)

        # Flyt eller kopier ansigtsbilledet til den tilsvarende mappe
        os.rename(face_image_path, destination_path)  # Eller brug shutil.copy()
        print(f"Ansigtsdata for {user_name} gemt til {destination_path}")

    def save_video_data(self, video_file_path):
        """Gemmer videodata i video-databasen."""
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        destination_path = os.path.join(self.video_db_path, f"video_{timestamp}.mp4")
        
        # Flyt eller kopier videofilen til database-mappen
        os.rename(video_file_path, destination_path)  # Eller brug shutil.copy()
        print(f"Video gemt til {destination_path}")

    def save_audio_data(self, audio_file_path):
        """Gemmer lyddata i lyd-databasen."""
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        destination_path = os.path.join(self.audio_db_path, f"audio_{timestamp}.mp3")
        
        # Flyt eller kopier lydfilen til database-mappen
        os.rename(audio_file_path, destination_path)  # Eller brug shutil.copy()
        print(f"Lyd gemt til {destination_path}")

    def add_emergency_contact(self, name, phone_number):
        """Tilføjer en nød-kontakt til databasen."""
        cursor = self.num_db.cursor()
        cursor.execute("INSERT INTO contacts (name, phone_number) VALUES (?, ?)", (name, phone_number))
        self.num_db.commit()
        print(f"Nød-kontakt '{name}' tilføjet med telefonnummer {phone_number}.")

    def list_emergency_contacts(self):
        """Viser alle nød-kontakter."""
        cursor = self.num_db.cursor()
        cursor.execute("SELECT name, phone_number FROM contacts")
        contacts = cursor.fetchall()
        if contacts:
            print("Nød-kontakter:")
            for contact in contacts:
                print(f"- {contact[0]}: {contact[1]}")
        else:
            print("Ingen nød-kontakter fundet.")

    def log_alarm(self, action, details):
        """Logger en alarmhandling i alarm-databasen."""
        cursor = self.alarm_db.cursor()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute("INSERT INTO alarms (timestamp, action, details) VALUES (?, ?, ?)", (timestamp, action, details))
        self.alarm_db.commit()
        print(f"Alarm logget: {action} kl. {timestamp}")

    def get_alarm_log(self):
        """Henter og viser alarm-loggen."""
        cursor = self.alarm_db.cursor()
        cursor.execute("SELECT * FROM alarms")
        logs = cursor.fetchall()
        if logs:
            print("Alarm-log:")
            for log in logs:
                print(f"ID: {log[0]} | Tidsstempel: {log[1]} | Handling: {log[2]} | Detaljer: {log[3]}")
        else:
            print("Ingen alarm-logs fundet.")
