class Dir:
    def __init__(self, name, files, dateCreated, dateModified, parent, size=0, index=0):
        self.index = index
        self.name = name
        self.size = size
        self.files = files
        self.dateCreated = dateCreated
        self.dateModified = dateModified
        self.parent = parent

    def structureDir(self):
        return { "directories" : {
                self.index : {
                "name" : self.name,
                "size" : self.size,
                "files" : self.files,
                "date_created" : self.dateCreated,
                "date_modified" : self.dateModified,
                "parent" : self.parent,
                }
               }
        }
