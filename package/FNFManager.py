from package.Core import Core
from package.Dir import Dir

class FNFManager(Core):
    def __init__(self):
        super().__init__()
        print(self.read_dir())

    def create_file(self):
        pass

    def delete_file(self):
        pass

    def open_file(self):
        pass

    def close_file(self):
        pass

    def show_map(self):
        pass

    def read_dir(self, dirname):
        directory = Dir(dirname)
        return directory.read()
