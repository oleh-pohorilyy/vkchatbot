import json
import os
from pathlib import Path


class Assets:
    dictionary = {}

    paths = {
        "assets": Path(__file__).parent / "../database/assets.json",
        "img": Path(__file__).parent / "../assets/img"
    }

    @staticmethod
    def load_resource_file():
        try:
            with open(Assets.paths["assets"], "r", encoding="utf-8") as f:
                Assets.dictionary = json.load(f)
        except Exception as e:
            print(e)

    @staticmethod
    def update_assets():
        for file_name in os.listdir(Assets.paths["img"]):
            img_path = Assets.get_resource_local_path(file_name)
            try:
                Assets.dictionary[file_name]
            except:
                photo = upload_photo(img_path, 0)["response"][0]
                Assets.dictionary[file_name] = f'photo{photo["owner_id"]}_{photo["id"]}'

    @staticmethod
    def save_assets():
        with open(Assets.paths["assets"], "w", encoding="utf-8") as f:
            json.dump(Assets.dictionary, f)

    @staticmethod
    def start(upload_photo):
        Assets.load_resource_file()
        Assets.update_assets()
        Assets.save_assets()

    @staticmethod
    def get_resource_local_path(name):
        return Assets.paths["img"] / name

    @staticmethod
    def get_resource_remote_path(name):
        try:
            return Assets.dictionary[name]
        except:
            return None
