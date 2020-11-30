import json
from files import File
import os.path
import sys

chunk_id = 0
file_id = 0
makeChanges = 0

def load_JSON():
    global JSON_structure
    if os.path.isfile('file_structure.json'):
        with open('file_structure.json') as JSON_Infile:
            JSON_structure = json.load(JSON_Infile)
            print(json.dumps(JSON_structure, indent=4))
    else:
        print("File not exist")


def create_file():
    global file_id
    file_name = input("Enter File name: ")
    file = File(file_id, file_name, 0, {})
    JSON_structure["files"].update(file.create_f())
    print("File Created Successfully!")
    print(json.dumps(JSON_structure, indent=4))
    file_id += 1


def delete_file():
    file_name = input("Enter File name: ")
    FnF = False
    for fileIndexes in JSON_structure["files"].keys():
        if JSON_structure["files"][fileIndexes]["name"] != file_name:
            FnF = True
        else:
            FnF = False
            JSON_structure["meta_data"]["storage"] -= JSON_structure["files"][fileIndexes]["size"]
            del JSON_structure["files"][fileIndexes]
    if FnF:
        print("File not found")
    print("File Deleted Successfully!")


def open_for_write(file_name):
    global makeChanges
    makeChanges = 1
    global chunk_id
    chunkSize = 20
    FnF = False
    for fileIndexes in JSON_structure["files"].keys():
        if JSON_structure["files"][fileIndexes]["name"] != file_name:
            FnF = True
        else:
            FnF = False
            Text = input("Enter Text: ")
            JSON_structure["files"][fileIndexes]["size"] += len(Text)
            JSON_structure["meta_data"]["storage"] += JSON_structure["files"][fileIndexes]["size"]
            for i in range(0, len(Text), chunkSize):
                JSON_structure["files"][fileIndexes]["chunks"].update({str(chunk_id): Text[i:i + chunkSize]})
                chunk_id += 1
            break
    if FnF:
        print("File not found")
    if not FnF:
        print("Data writing Successful!")


def open_for_read(file_name):
    fullData = ""
    FnF = False
    for fileIndexes in JSON_structure["files"].keys():
        if JSON_structure["files"][fileIndexes]["name"] != file_name:
            FnF = True
        else:
            FnF = False
            for data in JSON_structure["files"][fileIndexes]["chunks"].keys():
                fullData += JSON_structure["files"][fileIndexes]["chunks"][data] + " "
            break
    if FnF:
        print("File not found")
    if not FnF:
        print(fullData)


def open_file():
    while True:
        file_name = input("Enter file name: ")
        openOptions = "\n1. Open for Read\n2. Open for Write\n3. Close File"
        print(openOptions)
        openChoice = input("Enter value: ")
        if openChoice == "1":
            open_for_read(file_name)
        if openChoice == "2":
            open_for_write(file_name)
        if openChoice == "3":
            break


def show_map():
    pass


def dump_JSON():
    with open('file_structure.json', "w") as JSON_Outfile:
        json.dump(JSON_structure, JSON_Outfile, indent=4)


def close_program():
    if makeChanges > 0:
        print("Do you want save changes to file_structure.json?\n1.Yes\n2.No")
        haltInput = input("Enter value: ")
        if haltInput == "1":
            dump_JSON()
            sys.exit()
        elif haltInput == "2":
            sys.exit()
        else:
            print("Invalid input")
    else:
        sys.exit()


startProgram = 1
while True:
    if startProgram == 1:
        load_JSON()
    menu_options = "\n1. Create File\n2. Delete File\n3. Open File\n4. Show Map\n5. Kill Program"
    print(menu_options)
    user_choice = input("Enter value: ")
    if user_choice == "1":
        create_file()
    elif user_choice == "2":
        delete_file()
    elif user_choice == "3":
        open_file()
    elif user_choice == "4":
        show_map()
    elif user_choice == "5":
        close_program()
    else:
        print("Invalid input")
    startProgram += 1
