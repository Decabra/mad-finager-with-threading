import json
import threading
from files import File
import os.path
import sys

makeChanges = 0

Lock = threading.Lock()


class Threads(threading.Thread):
    FileName = None
    ThreadId = None

    def __init__(self, file_name, number):
        super().__init__()
        self.FileName = file_name
        self.ThreadId = number

    def run(self):
        # Get lock to synchronize threads
        Lock.acquire()
        print("Starting thread " + str(self.ThreadId))
        cmd_execute(self.FileName, self.ThreadId)
        # Free lock to release next thread
        Lock.release()


def file_id_assigner():
    if not list(JSON_structure["files"].keys()):
        file_id = 0
    else:
        file_id = int(list(JSON_structure["files"].keys())[-1])
        file_id += 1
    return file_id


def chunk_id_assigner(file_indexes):
    if not list(JSON_structure["files"][file_indexes]["chunks"].keys()):
        chunk_id = 0
    else:
        chunk_id = int(list(JSON_structure["files"][file_indexes]["chunks"].keys())[-1])
        chunk_id += 1
    return chunk_id


def load_JSON():
    global JSON_structure
    if os.path.isfile('file_structure.json'):
        with open('file_structure.json') as JSON_Infile:
            JSON_structure = json.load(JSON_Infile)
    else:
        print("JSON File not found")


def create_file(file_name):
    global makeChanges
    flag = False
    for fileIndexes in list(JSON_structure["files"]):
        if JSON_structure["files"][fileIndexes]["name"] == file_name:
            flag = True
            break
    if flag:
        print("File with the same name already Exists!")
    else:
        file = File(file_id_assigner(), file_name, 0, {})
        JSON_structure["files"].update(file.create_f())
        JSON_structure["meta_data"]["files"] += 1
        print("File Created Successfully!")
        makeChanges = 1


def delete_file(file_name):
    global makeChanges
    FnF = False
    for fileIndexes in list(JSON_structure["files"]):
        if JSON_structure["files"][fileIndexes]["name"] != file_name:
            FnF = True
        else:
            FnF = False
            JSON_structure["meta_data"]["storage"] -= JSON_structure["files"][fileIndexes]["size"]
            del JSON_structure["files"][fileIndexes]
            break
    if FnF:
        print("File not exists")
    if not FnF:
        print("File Deleted Successfully!")
        JSON_structure["meta_data"]["files"] -= 1
        makeChanges = 1


def open_for_write(file_name):
    global makeChanges
    makeChanges = 1
    chunkSize = 20
    FnF = False
    for file_indexes in JSON_structure["files"].keys():
        if JSON_structure["files"][file_indexes]["name"] != file_name:
            FnF = True
        else:
            FnF = False
            Text = input("Enter Text: ")
            JSON_structure["files"][file_indexes]["size"] += len(Text)
            JSON_structure["meta_data"]["storage"] += JSON_structure["files"][file_indexes]["size"]
            for i in range(0, len(Text), chunkSize):
                JSON_structure["files"][file_indexes]["chunks"].update(
                    {str(chunk_id_assigner(file_indexes)): Text[i:i + chunkSize]})
            break
    if FnF:
        print("File not exists")
    if not FnF:
        print("Data writing Successful!")


def open_for_read(file_name):
    fullData = ""
    FnF = False
    for file_indexes in JSON_structure["files"].keys():
        if JSON_structure["files"][file_indexes]["name"] != file_name:
            FnF = True
        else:
            FnF = False
            for data in JSON_structure["files"][file_indexes]["chunks"].keys():
                fullData += JSON_structure["files"][file_indexes]["chunks"][data] + ""
            break
    if FnF:
        print("File not exists")
    if not FnF:
        message = fullData if fullData else "File is empty!"
        print(message)


def open_file():
    file_name = input("Enter file name: ")
    while True:
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
    print(json.dumps(JSON_structure, indent=4))


def dump_JSON():
    with open('file_structure.json', "w") as JSON_Outfile:
        json.dump(JSON_structure, JSON_Outfile, indent=4)
        print("Changes Saved!")


def close_program():
    if makeChanges > 0:
        print("Do you want save changes to file_structure.json?\n1.Yes\n2.No")
        haltInput = input("Enter value: ")
        if haltInput == "1":
            dump_JSON()
        elif haltInput == "2":
            pass
        else:
            print("1. Invalid input")
    else:
        pass


def cmd_execute(cmd_file, thread_id):
    if os.path.isfile(cmd_file):
        with open(cmd_file, "r") as commands:
            cmd_list = commands.read().split("\n")
        for i in range(0, len(cmd_list), 1):
            cmd_kw = cmd_list[i].split(" ")
            if cmd_kw[0] == "create":
                create_file(cmd_kw[1])
            elif cmd_kw[0] == "delete":
                delete_file(cmd_kw[1])
            elif cmd_kw[0] == "open_for_read":
                open_for_read(cmd_kw[1])
            elif cmd_kw[0] == "open_for_write":
                open_for_write(cmd_kw[1])
            elif cmd_kw[0] == "show_map":
                show_map()
            elif cmd_kw[0] == "close":
                close_program()
            else:
                print("Invalid input")
        print("Finishing thread " + str(thread_id))
    else:
        print("Commands File not found")
    return


startProgram = 0
while True:
    if startProgram == 0:
        load_JSON()
    cmd_file = input("Enter Commands File: ")
    k = int(input("Enter no. of threads: "))
    thread_array = []
    for i in range(k):
        # Create new threads
        running_thread = Threads(cmd_file, i + 1)
        # Start new Threads
        running_thread.start()
        # Add threads to thread list
        thread_array.append(running_thread)

    # Wait for all threads to complete
    for t in thread_array:
        t.join()
    print("Exiting main thread...")
    startProgram = 1
    sys.exit()
