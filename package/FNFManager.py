from package.Core import Core


class FNFManager(Core):
    def __init__(self):
        super().__init__()
        print(self.read_dir())

    def read_dir(self, dir_name=""):
        # if there will be no directory then root directory data will be returned
        f_data = []
        data = self.get_db_data()
        directory = data["directories"]

        if directory:
            if not dir_name:
                return directory["0"]

        return f_data
