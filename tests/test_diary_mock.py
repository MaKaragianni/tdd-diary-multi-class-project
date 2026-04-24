from unittest.mock import Mock
from lib.diary import Diary

class FakeEntry:
    def __init__(self, numbers):
        self._numbers = numbers

    def extract_tel_numbers(self):
        return self._numbers

def test_all_tel_numbers_with_multiple_entries():
    diary = Diary()

    entry1 = FakeEntry(["07111111111"])
    entry2 = FakeEntry(["07222222222", "07333333333"])

    diary.add(entry1)
    diary.add(entry2)

    assert diary.all_tel_numbers() == [
        "07111111111",
        "07222222222",
        "07333333333"
    ]

def test_all_tel_numbers_calls_method_on_entries():
    diary = Diary()

    mock_entry = Mock() # Creates a fake object
    mock_entry.extract_tel_numbers.return_value = ["07123456789"] # When this method is called, return this

    diary.add(mock_entry)

    result = diary.all_tel_numbers()

    assert result == ["07123456789"]
    mock_entry.extract_tel_numbers.assert_called_once() # Verifies interaction, not just output