from package.FNFManager import FNFManager
from datetime import date


class Finager(FNFManager):
    def __init__(self):
        super().__init__()

    def print_menu(self):
        menu_options = """
        1. Create File
        2. Delete File
        3. Open File
        4. Close File
        5. Show Map"""

        print(menu_options)
        today = date.today()
        print(today)
        user_choice = input("Enter value: ")
        if user_choice == 1:
            self.create_file()
        elif user_choice == 2:
            self.delete_file()
        elif user_choice == 3:
            self.open_file()
        elif user_choice == 4:
            self.close_file()
        else:
            self.show_map()
