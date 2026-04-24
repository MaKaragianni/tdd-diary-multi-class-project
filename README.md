# TDD Diary Multi-Class

A Python project built using Test-Driven Development (TDD) to implement a multi-class diary and task management system.

## 🚀 Features

- Add, store and read diary entries  
- Calculate reading time based on words per minute  
- Select the best entry to read within a time limit  
- Extract phone numbers from diary entries  
- Manage a todo list with task completion tracking  

## 🧱 Project Structure

- lib/
- diary.py
- diary_entry.py
- todo_list.py
- task.py

tests/
- test_diary_entry.py
- test_diary_integration.py
- test_diary_mock.py
- test_todo_integration.py


## 🧠 Concepts Demonstrated

- Object-Oriented Programming (OOP)  
- Multi-class system design  
- Dependency injection & mocking  
- Test-Driven Development (TDD)  
- Unit and integration testing  

## 🧪 Running Tests

```bash
pytest
⚙️ Setup
python -m venv venv
source venv/bin/activate
pip install pytest
▶️ Example Usage
from lib.diary import Diary
from lib.diary_entry import DiaryEntry

diary = Diary()
diary.add(DiaryEntry("Call 07123456789"))

print(diary.all_tel_numbers())
# ["07123456789"]

📌 Notes
This project was built following a structured design recipe and the TDD workflow (red → green → refactor).
