# {{PROBLEM}} Multi-Class Planned Diary Design Recipe

## 1. Describe the Problem

We’re building a system with these capabilities:
Record diary entries
Read past entries
Select entries based on reading time (words per minute and available time)
Maintain a todo list
Extract all phone numbers (11 digits starting with 0) from diary entries

## 2. Design the Class System

┌────────────────────────────┐
│  Diary                     │
│ - entries                  │
│ - add(entry)               │
│ - all()                    │
│ - find_best_entry(wpm,mins)│
│ - all_tel_numbers()        │
└───────────┬────────────────┘
            │
            │ owns a list of
            ▼
        ┌─────────────────────────┐
        │ DiaryEntry              │
        │ - contents              │
        │ - count_words()         │
        │ - reading_time(wpm)     │
        │ - extract_tel_numbers() │
        └─────────────────────────┘
     tracks
    ▼
┌──────────────────────────┐
│ TodoList                 │
│ - _tasks                  │
│ - add(task)              │
│ - incomplete()           │
│ - complete()             │
└───────────┬──────────────┘
            ▼
┌────────────────────────────┐
│ Task                       │
│ - title                    │
│ - _complete()              │
│ - mark_complete()          │
│ - is_complete()            │
└────────────────────────────┘

```python
class Diary:
    # User-facing properties:
    #   _entries: list of DiaryEntry (or entry-like objects)

    def __init__(self):
        pass

    def add(self, entry):
        # Parameters:
        #   entry: DiaryEntry (or compatible object)
        # Side-effects:
        #   Adds the entry to the diary
        pass

    def all(self):
        # Returns:
        #   List of all diary entries
        pass

    def find_best_entry(self, wpm, minutes):
        # Parameters:
        #   wpm: int
        #   minutes: int
        # Returns:
        #   The best readable DiaryEntry for given time, or None
        pass

    def all_tel_numbers(self):
        # Returns:
        #   List of all tel numbers across all entries
        pass


class DiaryEntry:
    # User-facing properties:
    #   contents: string

    def __init__(self, contents):
        # Parameters:
        #   contents: string
        pass

    def count_words(self):
        # Returns:
        #   Integer word count
        pass

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: int
        # Returns:
        #   Reading time in minutes (rounded up)
        pass

    def extract_tel_numbers(self):
        # Returns:
        #   List of tel numbers (11 digits starting with 0)
        pass


class TodoList:
    # User-facing properties:
    #   _tasks: list of Task

    def __init__(self):
        pass

    def add(self, task):
        # Parameters:
        #   task: Task
        pass

    def incomplete(self):
        # Returns:
        #   List of incomplete Task objects
        pass


class Task:
    # User-facing properties:
    #   title: string

    def __init__(self, title):
        pass

    def mark_complete(self):
        # Side-effects:
        #   Marks task as complete
        pass

    def is_complete(self):
        # Returns:
        #   Boolean
        pass
```

## 3. Create Examples as Integration Tests

"""
Given a diary
When we add entries
We can retrieve them
"""
diary = Diary()
entry1 = DiaryEntry("Today I went out")
entry2 = DiaryEntry("I had coffee")
diary.add(entry1)
diary.add(entry2)
diary.all()  # => [entry1, entry2]


"""
Given multiple entries
When we select best entry for reading time
We get the most suitable one
"""
diary = Diary()
entry1 = DiaryEntry("one two three four")  # 4 words
entry2 = DiaryEntry("one two")             # 2 words
diary.add(entry1)
diary.add(entry2)

diary.find_best_entry(2, 1)  # => entry2


"""
Given diary entries with tel numbers
We can extract all tel numbers
"""
diary = Diary()
diary.add(DiaryEntry("Call 07123456789"))
diary.add(DiaryEntry("Call 07987654321"))

diary.all_tel_numbers() # => ["07123456789", "07987654321"]


"""
Given a todo list
When we add tasks
We can see incomplete tasks
"""
todo = TodoList()
task1 = Task("Buy milk")
task2 = Task("Walk dog")

todo.add(task1)
todo.add(task2)

todo.incomplete()  # => [task1, task2]


"""
Given a completed task
It is excluded from incomplete tasks
"""
task1.mark_complete()
todo.incomplete()  # => [task2]
```

## 4. Create Examples as Unit Tests

"""
DiaryEntry stores contents
"""
entry = DiaryEntry("Hello")
entry.contents  # => "Hello"


"""
Count words in entry
"""
entry = DiaryEntry("one two three")
entry.count_words()  # => 3


"""
Reading time calculation
"""
entry = DiaryEntry("one two three four")
entry.reading_time(2)  # => 2


"""
Extract tel numbers
"""
entry = DiaryEntry("Call 07123456789")
entry.extract_tel_numbers()  # => ["07123456789"]


"""
Task completion state
"""
task = Task("Buy milk")
task.is_complete()  # => False

task.mark_complete()
task.is_complete()  # => True


"""
Diary aggregates tel numbers (mocked dependency)
"""
class FakeEntry:
    def extract_tel_numbers(self):
        return ["07111111111"]

diary = Diary()
diary.add(FakeEntry())

diary.all_tel_numbers()  # => ["07111111111"]
```

## 5. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green,
refactor to implement the behaviour._
