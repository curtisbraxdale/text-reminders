from agenda.agenda import Agenda
import json

def save_agenda(agenda, filename="agenda.json"):
    with open(filename, "w") as f:
        json.dump(agenda.to_dict(), f, indent=4)

def load_agenda(path):
    with open(path, "r") as f:
        try:
            data = json.load(f)
            return Agenda.from_dict(data)
        except json.JSONDecodeError:
            print(f"Warning: {path} is empty or invalid. Starting with a new Agenda.")
            return Agenda()
