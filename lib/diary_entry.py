import math
import re

class DiaryEntry:
    def __init__(self, contents):
        self.contents = contents

    def count_words(self):
        return len(self.contents.split()) # len counts and .split() splits the string into words using spaces
    
    def reading_time(self, wpm):
        return math.ceil(self.count_words() / wpm) # If reading takes 1.5 min, the reader still needs 2 min
    
    def extract_tel_numbers(self):
        return re.findall(r"\b0\d{10}\b", self.contents)
    # Explanation:
        # \b → word boundary (avoids matching inside longer strings)
        # 0 → must start with 0
        # \d{10} → followed by exactly 10 digits
        # total = 11 digits
        # Matches: 07123456789

