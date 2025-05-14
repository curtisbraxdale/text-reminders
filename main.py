# main.py

import os
import json
from agenda.agenda import Agenda
from agenda.storage import save_agenda, load_agenda
from agenda.views import view_todos, view_cal_events, view_reminders
import questionary

DATA_FILE = os.path.join(os.path.dirname(__file__), "data", "agenda.json")

def main_menu():
    return questionary.rawselect(
        "What would you like to do?",
        choices=[
            "View Agenda",
            "Add Reminder",
            "Add Calendar Event",
            "Add Todo",
            "View Reminders",
            "View Calendar Events",
            "View ToDos",
            "Save and Exit"
        ]
    ).ask()

def load_or_init_agenda():
    if os.path.exists(DATA_FILE):
        return load_agenda(DATA_FILE)
    else:
        return Agenda()


def main():
    # Need to create or load from json file
    agenda = load_or_init_agenda()

    # Need to delete old Reminders, CalendarEvents, ToDo's
    agenda.delete_old_items()

    while True:
        choice = main_menu()

        if choice == "View Agenda":
            print(agenda.create_daily_agenda())
        elif choice == "Add Reminder":
            title = questionary.text("Reminder Title:").ask()
            date = questionary.text("Date (YYYY-MM-DD):").ask()
            level = questionary.rawselect("How important is this reminder?",
                choices=[
                    "Reminder appears in daily agenda.",
                    "Reminder appears in weekly & daily agenda."
                ]
            ).ask()
            recur_w = questionary.confirm("Do you want this reminder to recurr weekly?").ask()
            recur_m = questionary.confirm("Do you want this reminder to recurr monthly?").ask()
            print("Creating Reminder...")
            agenda.add_reminder(title, date, level, recur_w, recur_m)

        elif choice == "Add Calendar Event":
            title = questionary.text("Calendar Event Title:").ask()
            date = questionary.text("Date (YYYY-MM-DD):").ask()
            level = questionary.rawselect("How important is this Calendar Event?",
                choices=[
                    "Calendar Event appears in daily agenda.",
                    "Calendar Event appears in weekly & daily agenda."
                ]
            ).ask()
            multi_day = questionary.confirm("Is this a multi-day event?").ask()
            if(multi_day):
                end_date = questionary.text("End Date (YYYY-MM-DD):").ask()
                recur_y = questionary.confirm("Do you want this calendar event to recurr yearly?").ask()
                print("Creating Calendar Event...")
                agenda.add_calendar_event(title, date, level, recur_y, end_date)
            else:
                recur_y = questionary.confirm("Do you want this calendar event to recurr yearly?").ask()
                print("Creating Calendar Event...")
                agenda.add_calendar_event(title, date, level, recur_y)


        elif choice == "Add Todo":
            title = questionary.text("Task:").ask()
            date_due = questionary.text("Due Date (YYYY-MM-DD):").ask()
            print("Creating ToDo...")
            agenda.add_todo(title, date_due)

        elif choice == "View Reminders":
            view_reminders(agenda)

        elif choice == "View Calendar Events":
            view_cal_events(agenda)

        elif choice == "View ToDos":
            view_todos(agenda)

        elif choice == "Save and Exit":
            save_agenda(agenda, DATA_FILE)
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
