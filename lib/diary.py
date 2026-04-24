class Diary:
    def __init__(self):
        self._entries = []

    def add(self, entry):
        self._entries.append(entry)

    def all(self):
        return self._entries
    
    def find_best_entry(self, wpm, minutes):
        max_words = wpm * minutes
        readable_entries = [
            entry for entry in self._entries
            if entry.count_words() <= max_words # Calculate max readable words
        ]
        if not readable_entries:
            return None
        return max(readable_entries, key=lambda e: e.count_words()) # The lambda function gives us the entry with the highest wc
    
    def all_tel_numbers(self):
        numbers = []
        for entry in self._entries:
            numbers.extend(entry.extract_tel_numbers()) # .extend() adds multiple numbers from each entry
        return numbers
    