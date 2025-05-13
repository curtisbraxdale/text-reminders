from agenda.items import Reminder, CalendarEvent, ToDo

class Agenda:
    def __init__(self):
        self.reminders = []
        self.calendar_events = []
        self.todos = []

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
