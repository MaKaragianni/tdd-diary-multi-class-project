class Task:
    def __init__(self, title):
        self.title = title
        self._complete = False

    def mark_complete(self):
        self._complete = True

    def is_complete(self):
        return self._complete