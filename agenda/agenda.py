from agenda.items import Reminder, CalendarEvent, ToDo, agenda_item_factory
from datetime import date

class Agenda:
    def __init__(self):
        self.reminders = []
        self.calendar_events = []
        self.todos = []

    def to_dict(self):
        return {
            "reminders": [r.to_dict() for r in self.reminders],
            "calendar_events": [c.to_dict() for c in self.calendar_events],
            "todos": [t.to_dict() for t in self.todos]
        }

    def create_daily_agenda(self):
        day_agenda = f"{date.today().strftime('%A %b %d')}\n===============\n"
        if len(self.reminders) > 0:
            day_agenda += "~REMINDERS~\n"
            for reminder in self.reminders:
                if reminder.item_date == date.today():
                    #day_reminders.append(reminder)
                    day_agenda += f"{reminder.title}\n"
            day_agenda += "===============\n"
        if len(self.calendar_events) > 0:
            day_agenda += "~CALENDAR~\n"
            for event in self.calendar_events:
                if (event.item_date <= date.today()) and (event.end_date >= date.today()):
                    #day_events.append(event)
                    day_agenda += f"{event.title}\n"
            day_agenda += "===============\n"
        if len(self.todos) > 0:
            day_agenda += "~TO DO~\n"
            for todo in self.todos:
                day_agenda += f"{todo.title} (Due: {todo.due.strftime('%m-%d')})\n"
            day_agenda += "===============\n"
        return day_agenda

    def create_weekly_agenda(self):
        pass

    def add_reminder(self, title, date, level, recur_w, recur_m):
        self.reminders.append(Reminder(title, date, level, recur_w, recur_m))
        print("Reminder created!")
        return

    # Returns a list of 5 ToDo's starting at the given index.Agenda
    # Intended to act as a "page" of ToDo's.
    # If the desired ToDo is not in list, can be called again with bigger index.
    def view_todo_list(self, start, limit):
        return self.todos[start:start+limit]
    def view_calendar_list(self, start, limit):
        return self.calendar_events[start:start+limit]
    def view_reminder_list(self, start, limit):
        return self.reminders[start:start+limit]

    def add_calendar_event(self, title, date, level, recur_y, end_date=None):
        self.calendar_events.append(CalendarEvent(title, date, level, recur_y, end_date))
        print("Calendar Event created!")
        return

    def add_todo(self, title, due):
        self.todos.append(ToDo(title, due))
        print("ToDo created!")
        return

    def delete_old_items(self):
        pass

    @classmethod
    def from_dict(cls, data):
        agenda = cls()
        agenda.reminders = [agenda_item_factory(item) for item in data.get("reminders", [])]
        agenda.calendar_events = [agenda_item_factory(item) for item in data.get("calendar_events", [])]
        agenda.todos = [agenda_item_factory(item) for item in data.get("todos", [])]
        return agenda
