import questionary
from datetime import datetime, date


def view_todos(agenda):
    count = 0
    page_size = 5

    while True:
        choice_list = agenda.view_todo_list(count, page_size)
        choices = [
            f"{todo.title} (Due Date: {todo.due.strftime('%m-%d')})"
            for todo in choice_list
        ]

        # Navigation options
        if count + page_size < len(agenda.todos):
            choices.append("Next Page")
        if count > 0:
            choices.append("Previous Page")
        choices.append("Exit")

        selection = questionary.rawselect(
            "Which ToDo would you like to edit or delete?",
            choices=choices
        ).ask()

        if selection == "Next Page":
            count += page_size
        elif selection == "Previous Page":
            count -= page_size
        elif selection == "Exit":
            break
        else:
            index = choices.index(selection)
            selected_todo = choice_list[index]
            edit_or_delete_todo(agenda, selected_todo)
            break

def edit_or_delete_todo(agenda, todo):
    action = questionary.select(
        "What would you like to do?",
        choices=["Edit", "Delete", "Cancel"]
    ).ask()

    if action == "Edit":
        new_title = questionary.text("Enter new title:", default=todo.title).ask()
        new_due_str = questionary.text(
            "Enter new due date (YYYY-MM-DD):",
            default=todo.due.isoformat()
        ).ask()
        try:
            new_due = datetime.strptime(new_due_str, "%Y-%m-%d").date()
            todo.title = new_title
            todo.due = new_due
            print("ToDo updated!")
        except ValueError:
            print("Invalid date format. Edit canceled.")
    elif action == "Delete":
        agenda.todos.remove(todo)
        print("ToDo deleted.")
    else:
        print("Action canceled.")

def view_cal_events(agenda):
    count = 0
    page_size = 5

    while True:
        choice_list = agenda.view_calendar_list(count, page_size)
        choices = [
            f"{calendar_event.title} ({calendar_event.item_date.strftime('%m-%d')})"
            for calendar_event in choice_list
        ]

        # Navigation options
        if count + page_size < len(agenda.calendar_events):
            choices.append("Next Page")
        if count > 0:
            choices.append("Previous Page")
        choices.append("Exit")

        selection = questionary.rawselect(
            "Which Calendar Event would you like to edit or delete?",
            choices=choices
        ).ask()

        if selection == "Next Page":
            count += page_size
        elif selection == "Previous Page":
            count -= page_size
        elif selection == "Exit":
            break
        else:
            index = choices.index(selection)
            selected_calendar_event = choice_list[index]
            edit_or_delete_calendar_event(agenda, selected_calendar_event)
            break

def edit_or_delete_calendar_event(agenda, calendar_event):
    action = questionary.select(
        "What would you like to do?",
        choices=["Edit", "Delete", "Cancel"]
    ).ask()

    if action == "Edit":
        new_title = questionary.text("Enter new title:", default=calendar_event.title).ask()
        new_item_date_str = questionary.text(
            "Enter new date (YYYY-MM-DD):",
            default=calendar_event.item_date.isoformat()
        ).ask()
        new_level = questionary.rawselect("How important is this Calendar Event?",
            choices=[
                "Calendar Event appears in daily agenda.",
                "Calendar Event appears in weekly & daily agenda."
            ]
        ).ask()
        multi_day = questionary.confirm("Is this a multi-day event?").ask()
        if(multi_day):
            new_end_date_str = questionary.text("End Date (YYYY-MM-DD):").ask()
            new_recur_y = questionary.confirm("Do you want this calendar event to recurr yearly?").ask()
        else:
            new_end_date_str = new_item_date_str
            new_recur_y = questionary.confirm("Do you want this calendar event to recurr yearly?").ask()
        try:
            new_item_date = datetime.strptime(new_item_date_str, "%Y-%m-%d").date()
            new_end_date = datetime.strptime(new_end_date_str, "%Y-%m-%d").date()
            calendar_event.title = new_title
            calendar_event.item_date = new_item_date
            calendar_event.level = new_level
            calendar_event.recur_y = new_recur_y
            calendar_event.end_date = new_end_date
            print("Calendar Event updated!")
        except ValueError:
            print("Invalid date format. Edit canceled.")
    elif action == "Delete":
        agenda.calendar_events.remove(calendar_event)
        print("Calendar Event deleted.")
    else:
        print("Action canceled.")


def view_reminders(agenda):
    count = 0
    page_size = 5

    while True:
        choice_list = agenda.view_reminder_list(count, page_size)
        choices = [
            f"{reminder.title}"
            for reminder in choice_list
        ]

        # Navigation options
        if count + page_size < len(agenda.reminders):
            choices.append("Next Page")
        if count > 0:
            choices.append("Previous Page")
        choices.append("Exit")

        selection = questionary.rawselect(
            "Which Reminder would you like to edit or delete?",
            choices=choices
        ).ask()

        if selection == "Next Page":
            count += page_size
        elif selection == "Previous Page":
            count -= page_size
        elif selection == "Exit":
            break
        else:
            index = choices.index(selection)
            selected_reminder = choice_list[index]
            edit_or_delete_reminder(agenda, selected_reminder)
            break

def edit_or_delete_reminder(agenda, reminder):
    action = questionary.select(
        "What would you like to do?",
        choices=["Edit", "Delete", "Cancel"]
    ).ask()

    if action == "Edit":
        new_title = questionary.text("Enter new title:", default=reminder.title).ask()
        new_item_date_str = questionary.text(
            "Enter new date (YYYY-MM-DD):",
            default=reminder.item_date.isoformat()
        ).ask()
        new_level = questionary.rawselect("How important is this reminder?",
            choices=[
                "Reminder appears in daily agenda.",
                "Reminder appears in weekly & daily agenda."
            ]
        ).ask()
        new_recur_w = questionary.confirm("Do you want this reminder to recurr weekly?").ask()
        new_recur_m = questionary.confirm("Do you want this reminder to recurr monthly?").ask()
        try:
            new_item_date = datetime.strptime(new_item_date_str, "%Y-%m-%d").date()
            reminder.title = new_title
            reminder.item_date = new_item_date
            reminder.level = new_level
            reminder.recur_w = new_recur_w
            reminder.recur_m = new_recur_m
            print("Reminder updated!")
        except ValueError:
            print("Invalid date format. Edit canceled.")
    elif action == "Delete":
        agenda.reminders.remove(reminder)
        print("Reminder deleted.")
    else:
        print("Action canceled.")
