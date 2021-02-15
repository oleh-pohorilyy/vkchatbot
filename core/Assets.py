import json
import os
from pathlib import Path


class Assets:
    dictionary = {}

    pathes = {
        "assets": Path(__file__).parent / "../database/assets.json",
        "img": Path(__file__).parent / "../assets/img"
    }

    @staticmethod
    def start(upload_photo):
        with Assets.pathes["assets"].open("r", encoding="utf-8") as f:
            Assets.dictionary = json.load(f)

        for file_name in os.listdir(Assets.pathes["img"]):
            img_path = Assets.get_resource_path(file_name)
            try:
                Assets.dictionary[file_name]
            except:
                photo = upload_photo(img_path, 0)["response"][0]
                Assets.dictionary[file_name] = f'photo{photo["owner_id"]}_{photo["id"]}'

        with open(Assets.pathes["assets"], "w", encoding="utf-8") as f:
            json.dump(Assets.dictionary, f)

    @staticmethod
    def get_resource_path(name):
        return Path(Assets.pathes["img"]) / name

    @staticmethod
    def get_resource_remote_path(name):
        try:
            return Assets.dictionary[name]
        except:
            return None
