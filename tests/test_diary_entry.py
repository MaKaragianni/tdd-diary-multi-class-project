from lib.diary_entry import DiaryEntry

def test_count_words():
    entry = DiaryEntry("one two three")
    assert entry.count_words() == 3

def test_reading_time():
    entry = DiaryEntry("one two three four")
    assert entry.reading_time(2) == 2 # 4 words, 2 words per min

def test_extracts_single_tel_number():
    entry = DiaryEntry("Call me on 07123456789")
    assert entry.extract_tel_numbers() == ["07123456789"]

def test_extracts_multiple_tel_numbers():
    entry = DiaryEntry("Call 07123456789 or 07987654321")
    assert entry.extract_tel_numbers() == ["07123456789", "07987654321"]