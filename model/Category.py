class Category(object):

    def __init__(self, title, entries):
        self.title = title
        self.entries = entries

    def addEntry(self, entry):
        self.entries.append(entry)