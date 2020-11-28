import json


class Dir:
    def __init__(self, index, name, size, files, dateCreated, dateModified, parent):
        self.index = index
        self.name = name
        self.size = size
        self.files = files
        self.dateCreated = dateCreated
        self.dateModified = dateModified
        self.parent = parent

