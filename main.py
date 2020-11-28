import json
from dir import Dir
from files import Files
from datetime import date

menuOptions = """
1. Create File
2. Delete File
3. Open File
4. Close File
5. Show Map"""
print(menuOptions)
today = date.today()
print(today)
userChoice = input("Enter value: ")
today = date.today()

def create_file():
    pass


#    open("structure.json")
#    file_name = input("Enter path or filename: ")
def delete_file():
    pass


def open_file():
    pass


def close_file():
    pass


def show_map():
    pass

if userChoice == 1:
    create_file()
elif userChoice == 2:
    delete_file()
elif userChoice == 3:
    open_file()
elif userChoice == 4:
    close_file()
else:
    show_map()

