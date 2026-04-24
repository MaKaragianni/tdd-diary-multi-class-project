class TodoList:
    def __init__(self):
        self._tasks = []

    def add(self, task):
        self._tasks.append(task)

    def incomplete(self):
        return [task for task in self._tasks if not task.is_complete()]
    