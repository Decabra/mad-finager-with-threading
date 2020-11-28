class Dir:
    path = '/'

    def __init__(self, path):
        self.path = path

    def setDirectory(self, path):
        self.path = path

    def getDirectory(self):
        return self.path
