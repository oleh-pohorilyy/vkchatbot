import json
import os
from pathlib import Path
import copy
from Timer import Timer
from utils import u_find
from Assets import Assets

class Users:
    usermap = {}
    list = []
    users_path = Path(__file__).parent / "../database/users.json"
    usermap_path = Path(__file__).parent / "../database/usermap.json"

    @staticmethod
    def load_users(send_report):
        try:
            with Users.usermap_path.open("r", encoding="utf-8") as f:
                Users.usermap = json.load(f)
        except:
            send_report("Обосралась юзер мапа!")

        try:
            with open(Users.users_path, "r", encoding="utf-8") as f:
                Users.list = json.load(f)
        except:
            with open(Users.users_path, "w", encoding="utf-8") as f:
                json.dump([], f)

    @staticmethod
    def print_users():
        print(Users.list)

    @staticmethod
    def get_by_id(id):
        return u_find(lambda u, _: u["id"] == id, Users.list)

    @staticmethod
    def exists(id):
        return Users.get_by_id(id) is not None

    @staticmethod
    def register(ctx):
        new_user = copy.deepcopy(Users.usermap)
        new_user["id"] = ctx.message["from_id"]
        new_user["bot_id"] = len(Users.list)+1
        Users.list.append(new_user)
        Users.save_users_to_file()

    @staticmethod
    def register_if_not_registered(ctx):
        if not Users.exists(ctx.message["from_id"]):
            Users.register(ctx)


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
    def start(send_report):
        Users.load_users(send_report)
        Users.change_users_template()
        Users.run_autosaving()