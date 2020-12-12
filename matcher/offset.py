class OffsetData:
    def __init__(self, line_offset, char_offset):
        self.line_offset = line_offset
        self.char_offset = char_offset

    def to_string(self):
        return "lineOffset={}, charOffset={}".format(self.line_offset, self.char_offset)
