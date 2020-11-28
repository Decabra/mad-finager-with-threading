class Dir:
    def __init__(self, id, name, files, date_created, date_modified, parent, size=0, index=0):
        self.id = id
        self.index = index
        self.name = name
        self.size = size
        self.files = files
        self.date_created = date_created
        self.date_modified = date_modified
        self.parent = parent

    def dir_structure(self):
        return {
            self.index: {
                "id": self.id,
                "name": self.name,
                "size": self.size,
                "files": self.files,
                "date_created": self.date_created,
                "date_modified": self.date_modified,
                "parent": self.parent,
            }
        }
