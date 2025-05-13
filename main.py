# main.py

import os
from agenda.agenda import Agenda
#from agenda.storage import save_agenda, load_agenda
from agenda.items import CalendarEvent, Reminder, ToDo
import questionary

def main_menu():
    return questionary.rawselect(
        "What would you like to do?",
        choices=[
            "View Agenda",
            "Add Reminder",
            "Add Calendar Event",
            "Add Todo",
            "Save and Exit"
        ]
    ).ask()


def main():
    agenda = Agenda()

    while True:
        choice = main_menu()

        if choice == "View Agenda":
            pass
        elif choice == "Add Reminder":
            title = questionary.text("Reminder Title:").ask()
            date = questionary.text("Date (DD-MM-YY):").ask()
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
            date = questionary.text("Date (DD-MM-YY):").ask()
            level = questionary.rawselect("How important is this reminder?",
                choices=[
                    "Calendar Event appears in daily agenda.",
                    "Calendar Event appears in weekly & daily agenda."
                ]
            ).ask()
            multi_day = questionary.confirm("Is this a multi-day event?").ask()
            if(multi_day):
                end_date = questionary.text("End Date (DD-MM-YY):").ask()
                recur_y = questionary.confirm("Do you want this calendar event to recurr yearly?").ask()
                print("Creating Calendar Event...")
                agenda.add_calendar_event(title, date, level, recur_y, end_date)
            else:
                recur_y = questionary.confirm("Do you want this calendar event to recurr yearly?").ask()
                print("Creating Calendar Event...")
                agenda.add_calendar_event(title, date, level, recur_y)


        elif choice == "Add Todo":
            title = questionary.text("Task:").ask()
            date_due = questionary.text("Due Date (DD-MM-YY):").ask()
            print("Creating ToDo...")
            agenda.add_todo(title, date_due)

        elif choice == "Save and Exit":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
