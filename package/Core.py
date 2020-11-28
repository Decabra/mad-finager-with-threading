import os
import json
from datetime import datetime


def get_init_db_data():
    current_timestamp = str(datetime.now())
    return {
        "meta_data": {
            "storage": 0,
            "directories": 0,
            "files": 0
        },
        "directories": {
            "0": {
                "files": {},
                "name": "root",
                "created_at": current_timestamp,
                "modified_at": current_timestamp,
                "size": 0,
                "parent": 0
            }
        },
        "files": {},
        "chunks": {}
    }


class Core:
    db = os.getcwd() + "/db.json"
    data = ""

    def __init__(self):
        if not self.is_db_exist():
            self.create_db()
        else:
            self.load_db()

    def is_db_exist(self):
        return os.path.isfile(self.db)

    def create_db(self):
        with open(self.db, "w") as file:
            db_data = get_init_db_data()
            file.write(json.dumps(db_data))
            self.set_db_data(db_data)

    def load_db(self):
        with open(self.db) as file:
            self.set_db_data(json.loads(file.read()))

    def set_db_data(self, data):
        self.data = data

    def get_db_data(self):
        return self.data
