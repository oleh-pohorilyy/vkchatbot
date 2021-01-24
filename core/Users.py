import json
import os
from pathlib import Path
import copy
from Timer import Timer


class Users:
    items = {}
    usermap = {}
    list = []
    users_path = Path(__file__).parent / "../database/users.json"
    usermap_path = Path(__file__).parent / "../database/usermap.json"
    items_path = Path(__file__).parent / "../database/items.json"


    @staticmethod
    def load_items():
        with Users.items_path.open("r", encoding="utf-8") as f:
            Users.items = json.load(f)


    @staticmethod
    def load_users():
        if not os.path.exists(Users.users_path):
            with open(Users.users_path, "w", encoding="utf-8") as f:
                json.dump([], f)
        with Users.usermap_path.open("r", encoding="utf-8") as f:
            Users.usermap = json.load(f)
        with Users.users_path.open("r", encoding="utf-8") as f:
            Users.list = json.load(f)

    @staticmethod
    def print_users():
        print(Users.list)

    @staticmethod
    def get_by_id(id):
        for user in Users.list:
            if user["id"] == id:
                return user
        return None

    @staticmethod
    def exists(id):
        return Users.get_by_id(id) is not None

    @staticmethod
    def register(id):
        new_user = copy.deepcopy(Users.usermap)
        new_user["id"] = id
        new_user["bot_id"] = len(Users.list)+1
        Users.list.append(new_user)
        Users.save_users_to_file()

    @staticmethod
    def check_registered(id):       # id это id пользователя, который мы получаем в файле VK
        if not Users.exists(id):
            Users.register(id)

    @staticmethod
    def save_users_to_file():
        with open(Users.users_path, "w", encoding="utf-8") as f:
            json.dump(Users.list, f)
            print('Users saved!')

    @staticmethod
    def run_autosaving():
        Timer(Users.save_users_to_file, 60.0).start()

    @staticmethod
    def change_value(id, key, value):
        Users.get_by_id(id)[key] = value

    @staticmethod
    def change_users_template():
        for user in Users.list:
            blank = {}
            for key in Users.usermap:
                try:
                    blank[key] = user[key]
                except:
                    blank[key] = Users.usermap[key]
            user.clear()
            user.update(blank)
        Users.save_users_to_file()

    @staticmethod
    def start():
        Users.load_items()
        Users.load_users()
        Users.change_users_template()
        Users.run_autosaving()