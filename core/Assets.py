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
                Assets.dictionary[file_name]["remote"]
            except Exception as e:
                Assets.dictionary[file_name] = {
                    "remote": None,
                    "local": img_path
                }
            finally:
                photo = upload_photo(img_path, 0)["response"][0]
                Assets.dictionary[file_name]["remote"] = f'photo{photo["owner_id"]}_{photo["id"]}'
                print(Assets.dictionary)

    @staticmethod
    def get_resource_path(name):
        try:
            return Path(Assets.pathes["img"]) / name
        except:
            return None