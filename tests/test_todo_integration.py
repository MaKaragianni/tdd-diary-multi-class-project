from lib.todo_list import TodoList
from lib.task import Task

def test_add_and_list_incomplete_tasks():
    todo = TodoList()

    task1 = Task("Buy milk")
    task2 = Task("Walk dog")

    todo.add(task1)
    todo.add(task2)

    assert todo.incomplete() == [task1, task2]

def test_complete_tasks_are_removed_from_incomplete():
    todo = TodoList()

    task1 = Task("Buy milk")
    task2 = Task("Walk dog")

    todo.add(task1)
    todo.add(task2)

    task1.mark_complete()

    assert todo.incomplete() == [task2]

    