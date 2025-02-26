from liveFeed import LiveFeed
from databaseManager import DatabaseManager

class CameraSystem:
    def __init__(self):
        """Initialiserer kamera systemet med alle komponenter."""
        self.running = True
        self.db_manager = DatabaseManager()
        self.live_feed = LiveFeed(self.db_manager)
        self.live_feed_thread = None

    def display_menu(self):
        """Viser hovedmenuen."""
        print("\n--- Hovedmenu ---")
        print("1. Registrer ansigt")
        print("2. Registrer telefonnummer")
        print("3. Start live-feed")
        print("4. Vis nød-kontakter")
        print("5. Vis alarm-log")
        print("6. Afslut")

    def run_face_registry(self):
        """Kører processen for registrering af ansigt."""
        print("\n--- Registrering af ansigt ---")
        user_name = input("Indtast brugernavn for at registrere ansigt: ").strip()
        if not user_name:
            print("Brugernavn kan ikke være tomt. Prøv igen.")
            return
        try:
            self.db_manager.face_recorder.initialize_user(user_name)
            print(f"Registrerer ansigter for {user_name}...")
            self.db_manager.face_recorder.run()
            print(f"Ansigter for {user_name} er registreret.")
        except Exception as e:
            print(f"Fejl under registrering af ansigt: {e}")

    def register_phone_number(self):
        """Registrerer et telefonnummer."""
        print("\n--- Registrering af telefonnummer ---")
        try:
            self.db_manager.num_db.run()
        except Exception as e:
            print(f"Fejl under registrering af telefonnummer: {e}")

    def start_live_feed(self):
        """Starter live-feed og tillader afbrydelser."""
        print("\n--- Starter live-feed ---")
        try:
            # Starter live-feed i en ny tråd for at tillade brugerafbrydelse
            if self.live_feed_thread is None or not self.live_feed_thread.is_alive():
                self.live_feed_thread = self.live_feed.run_in_thread()
            else:
                print("Live-feed kører allerede.")
        except Exception as e:
            print(f"Fejl under live-feed: {e}")

    def list_emergency_contacts(self):
        """Viser nød-kontakter."""
        print("\n--- Nød-kontakter ---")
        self.db_manager.num_db.list_contacts()

    def view_alarm_log(self):
        """Viser alarm-log."""
        print("\n--- Alarm-log ---")
        self.db_manager.alarm_db.view_log()

    def run(self):
        """Kører menuen og håndterer brugerinput med mulighed for at afslutte programmet."""
        while self.running:
            self.display_menu()
            choice = input("Indtast valg: ").strip()

            if choice == "1":
                self.run_face_registry()
            elif choice == "2":
                self.register_phone_number()
            elif choice == "3":
                self.start_live_feed()
            elif choice == "4":
                self.list_emergency_contacts()
            elif choice == "5":
                self.view_alarm_log()
            elif choice == "6":
                print("Afslutter...")
                self.stop_live_feed()
            else:
                print("Ugyldigt valg. Prøv igen.")

    def stop_live_feed(self):
        """Stopper live-feedet på en kontrolleret måde, hvis det kører."""
        if self.live_feed_thread and self.live_feed_thread.is_alive():
            print("Stopper live-feed...")
            self.live_feed_thread.join()  # Venter på, at live-feed tråden afslutter
        else:
            print("Intet live-feed kører i øjeblikket.")
