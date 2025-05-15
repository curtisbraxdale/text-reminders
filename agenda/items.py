from datetime import date, timedelta

class AgendaItem:
    def __init__(self, title, item_date):
        self.title = title
        self.date = date.fromisoformat(item_date)

    def to_dict(self):
        return {
            "type": self.__class__.__name__,
            "title": self.title,
            "date": self.date
            }

    @classmethod
    def from_dict(cls, data):
        return cls(data["title"], data["date"])

class CalendarEvent(AgendaItem):
    def __init__(self, title, item_date, level=1, recur_y=False, end_date=None):
        self.title = title
        self.item_date = date.fromisoformat(item_date)
        self.level = level
        self.recur_y = recur_y
        self.end_date = date.fromisoformat(end_date) if end_date else self.item_date


    def to_dict(self):
        return {
            "type": "CalendarEvent",
            "title": self.title,
            "item_date": self.item_date.isoformat(),
            "level": self.level,
            "recur_y": self.recur_y,
            "end_date": self.end_date.isoformat()
        }

    def is_this_week(self):
        today = date.today()
        start = today - timedelta(days=today.weekday())
        end = start + timedelta(days=6)
        return start <= self.item_date <= end

    @classmethod
    def from_dict(cls, data):
        return cls(
            title=data["title"],
            item_date=data["item_date"],
            level=data.get("level", 1),
            recur_y=data.get("recur_y", False),
            end_date=data["end_date"],
        )

class Reminder(AgendaItem):
    def __init__(self, title, item_date, level=1, recur_w=False, recur_m=False):
        self.title = title
        self.item_date = date.fromisoformat(item_date)
        self.level = level
        self.recur_w = recur_w
        self.recur_m = recur_m


    def to_dict(self):
        return {
            "type": "Reminder",
            "title": self.title,
            "item_date": self.item_date.isoformat(),
            "level": self.level,
            "recur_w": self.recur_w,
            "recur_m": self.recur_m
        }

    def is_this_week(self):
        today = date.today()
        start = today - timedelta(days=today.weekday())
        end = start + timedelta(days=6)
        return start <= self.item_date <= end

    @classmethod
    def from_dict(cls, data):
        return cls(
            title=data["title"],
            item_date=data["item_date"],
            level=data.get("level", 1),
            recur_w=data.get("recur_w", False),
            recur_m=data.get("recur_m", False)
        )

class ToDo(AgendaItem):
    def __init__(self, title, due):
        self.title = title
        self.due = date.fromisoformat(due)

    def to_dict(self):
        return {
            "type": "ToDo",
            "title": self.title,
            "due": self.due.isoformat(),
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            title=data["title"],
            due=data["due"],
        )

def agenda_item_factory(data):
    item_type = data["type"]
    if item_type == "CalendarEvent":
        return CalendarEvent.from_dict(data)
    elif item_type == "Reminder":
        return Reminder.from_dict(data)
    elif item_type == "ToDo":
        return ToDo.from_dict(data)
    else:
        raise ValueError(f"Unknown AgendaItem type: {item_type}")
