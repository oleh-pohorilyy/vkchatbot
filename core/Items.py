from pathlib import Path
import json


class Items:
    dictionary = {}
    items_path = Path(__file__).parent / "../database/items.json"

    @staticmethod
    def start():
        with Items.items_path.open("r", encoding="utf-8") as f:
            Items.dictionary = json.load(f)

    @staticmethod
    def get_by_id(id):
        return Items.dictionary[str(id)]
