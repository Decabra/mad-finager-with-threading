from package.Core import Core


class Dir(Core):
    path = '/'
    id = 0
    name = ''
    size = 0
    files = ''
    date_created = ''
    date_modified = ''
    parent = 0

    def __init__(self, path):
        super().__init__()
        self.path = path

    def process(self, id, name, files, date_created, date_modified, parent, size=0):
        self.id = id
        self.name = name
        self.size = size
        self.files = files
        self.date_created = date_created
        self.date_modified = date_modified
        self.parent = parent

    def dir_structure(self):
        return {
            self.id: {
                "name": self.name,
                "size": self.size,
                "files": self.files,
                "date_created": self.date_created,
                "date_modified": self.date_modified,
                "parent": self.parent,
            }
        }

    def setDirectory(self, path):
        self.path = path

    def getDirectory(self):
        return self.path

    def getDirectoryList(self):
        data = self.get_db_data()
        return data["directories"]

    def read(self):
        # if there will be no directory then root directory data will be returned
        directory = self.getDirectoryList()

        if directory:
            # this will go through the process of reading a file path
            # a path can have many directories to move inside
            path = self.getDirectory()
            path = path.split('/')
            # loop through each part of a single path
            for part in path:
                self.readDirectory(part)
            return False

    def readDirectory(self, dirname):
        directory_list = self.getDirectoryList()
        for directory in directory_list:
            if directory.name == dirname:
                pass

        return False
