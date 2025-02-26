import logging


class ErrorHandling:
    def __init__(self):
        # Konfigurer logningsformat
        logging.basicConfig(filename='robot_errors.log', level=logging.ERROR,
                            format='%(asctime)s - %(levelname)s - %(message)s')

    def log_error(self, error_message):
        logging.error(error_message)

    def handle_error(self, exception, critical=False):
        if critical:
            # Kritiske fejl kræver stop af programmet
            logging.critical(f"Critical error occurred: {exception}")
            print(f"Critical error: {exception}. Stopping the system!")
            exit(1)
        else:
            # Ikke-kritiske fejl kan logges og behandles
            logging.warning(f"Non-critical error: {exception}")
            print(f"Warning: {exception}. The system will attempt to recover.")


# Eksempel på at bruge ErrorHandling-klassen
if __name__ == "__main__":
    error_handler = ErrorHandling()

    try:
        # Simulerer en fejl (f.eks. en sensor der fejler)
        raise ValueError("Sensor malfunction!")
    except Exception as e:
        error_handler.handle_error(e)
