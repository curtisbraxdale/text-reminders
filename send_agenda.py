from agenda.storage import load_agenda
from agenda.messaging import send_agenda_text
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), "data", "agenda.json")

def main():
    agenda = load_agenda(DATA_FILE)
    send_agenda_text(agenda)  # This function formats and sends the agenda via text

if __name__ == "__main__":
    main()
