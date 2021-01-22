import json
import os
from pathlib import Path
import copy

class Users:
    usermap = {}
    list = []
    users_path = Path(__file__).parent / "../database/users.json"
    usermap_path = Path(__file__).parent / "../database/usermap.json"

    @staticmethod
    def load_users():
        if not os.path.exists(Users.users_path):
            with open(Users.users_path, "w", encoding="urf-8") as f:
                json.dump([], f)
        with Users.usermap_path.open() as f:
            Users.usermap = json.load(f)
        with Users.users_path.open() as f:
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

    @staticmethod
    def change_value(id, key, value):
        for user in Users.list:
            if user["id"] == id:
                user[key] = value
        Users.save_users_to_file()

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