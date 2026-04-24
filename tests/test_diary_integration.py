from lib.diary import Diary
from lib.diary_entry import DiaryEntry

def test_add_and_list_entries():
    diary = Diary()
    entry1 = DiaryEntry("Today I went to the park")
    entry2 = DiaryEntry("I had coffee")

    diary.add(entry1)
    diary.add(entry2)

    assert diary.all() == [entry1, entry2]

def test_find_best_entry_for_reading_time():
    diary = Diary()

    entry1 = DiaryEntry("one two three four")
    entry2 = DiaryEntry("one two")

    diary.add(entry1)
    diary.add(entry2)

    best = diary.find_best_entry(2, 1)  # 2 wpm = 1 min so best for shorter time

    assert best == entry2

def test_diary_returns_all_tel_numbers():
    diary = Diary()

    entry1 = DiaryEntry("Call 07123456789")
    entry2 = DiaryEntry("Emergency 07987654321")

    diary.add(entry1)
    diary.add(entry2)

    assert diary.all_tel_numbers() == ["07123456789", "07987654321"]

def test_diary_returns_empty_list_if_no_numbers():
    diary = Diary()
    diary.add(DiaryEntry("No phone numbers here"))

    assert diary.all_tel_numbers() == []