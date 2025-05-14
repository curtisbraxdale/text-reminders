from agenda.items import Reminder, CalendarEvent, ToDo, agenda_item_factory

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

    def create_daily_agenda():
        pass

    def create_weekly_agenda():
        pass

    def add_reminder(self, title, date, level, recur_w, recur_m):
        self.reminders.append(Reminder(title, date, level, recur_w, recur_m))
        print("Reminder created!")
        return

    def add_calendar_event(self, title, date, level, recur_y, end_date=None):
        self.calendar_events.append(CalendarEvent(title, date, level, recur_y, end_date))
        print("Calendar Event created!")
        return

    def add_todo(self, title, due):
        self.todos.append(ToDo(title, due))
        print("ToDo created!")
        return

    def delete_old_items(self):

        return

    @classmethod
    def from_dict(cls, data):
        agenda = cls()
        agenda.reminders = [agenda_item_factory(item) for item in data.get("reminders", [])]
        agenda.calendar_events = [agenda_item_factory(item) for item in data.get("calendar_events", [])]
        agenda.todos = [agenda_item_factory(item) for item in data.get("todos", [])]
        return agenda
