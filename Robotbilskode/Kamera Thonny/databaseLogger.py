import os
import threading
from datetime import datetime

class DatabaseLogger:
    def __init__(self, log_db_path="logs"):
        """Initialiserer loggeren med en specifik log-mappe."""
        self.log_db_path = log_db_path
        self.lock = threading.Lock()  # Sikrer trådsikre skriverutiner
        os.makedirs(self.log_db_path, exist_ok=True)

    def save_log(self, message):
        """Gemmer en log-besked i en log-fil i den angivne mappe."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file = os.path.join(self.log_db_path, "log.txt")
        
        # Trådsikker filskrivning
        with self.lock:
            with open(log_file, "a") as f:
                f.write(f"{timestamp}: {message}\n")
        print(f"Log gemt: {message}")
