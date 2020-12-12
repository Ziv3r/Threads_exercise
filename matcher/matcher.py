import os

from matcher.offset import OffsetData


class Matcher:
    def __init__(self, text_to_find_matches, words_to_look_for, starting_line, starting_char):
        self.text_to_find_matches = text_to_find_matches
        self.words_to_look_for = words_to_look_for
        self.starting_line = starting_line
        self.starting_char = starting_char
        self.word_to_locations = {}  # word to list of offsets

    # Think how to solve the bug of that it will return the first occurence always !
    def find_matches(self):
        for line in self.text_to_find_matches:
            self.starting_line += 1
            for word in line.split(" "):
                if word in self.words_to_look_for:
                    # create offset_data object
                    line_offset = self.starting_line
                    char_offset = line.find(word) + self.starting_char
                    offset = OffsetData(line_offset, char_offset)
                    self.word_to_locations[word] = offset

            self.starting_char += len(line)

    def print_dict(self):
        print(self.word_to_locations)
