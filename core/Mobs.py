from pathlib import Path
import json

class Mobs:
    dictionary = {}
    mobs_path = Path(__file__).parent / "../database/mobs.json"

    @staticmethod
    def start():
        with Mobs.mobs_path.open("r", encoding="utf-8") as f:
            Mobs.dictionary = json.load(f)

    @staticmethod
    def get_by_id(id):
        return Mobs.dictionary[str(id)]