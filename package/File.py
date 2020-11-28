class File:
    def __init__(self, index, id, name, date_modified, date_created, size):
        self.index = index
        self.id = id
        self.name = name
        self.date_modified = date_modified
        self.date_created = date_created
        self.size = size

    def file_structure(self):
        return {
            self.index: {
                "id": self.id,
                "name": self.name,
                "size": self.size,
                "date_created": self.date_created,
                "date_modified": self.date_modified
            }
        }

    def chunks(self, index, data):
        return {
            self.id: {
                index: data
            }
        }
