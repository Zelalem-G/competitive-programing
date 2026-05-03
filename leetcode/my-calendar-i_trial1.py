class MyCalendar(object):

    def __init__(self):
        self.events = []

    def book(self, start, end):
        for s, e in self.events:
            if start < e and end > s:
                return False

        self.events.append((start, end))
        return True