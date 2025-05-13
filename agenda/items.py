class AgendaItem:
    def __init__(self, title, date):
        self.title = title
        self.date = date

class CalendarEvent(AgendaItem):
    def __init__(self, title, date, level, recur_y=False, end_date=None):
        self.title = title
        self.date = date
        self.level = level
        self.recur_y = recur_y
        self.end_date = end_date

class Reminder(AgendaItem):
    def __init__(self, title, date, level, recur_w=False, recur_m=False):
        self.title = title
        self.date = date
        self.level = level
        self.recur_w = recur_w
        self.recur_m = recur_m

class ToDo(AgendaItem):
    def __init__(self, title, due):
        self.title = title
        # set date = time created by default
        # self.date =
        self.due = due
