from pathlib import Path
import json

class Locations:
    dictionary = {}
    locations_path = Path(__file__).parent / "../database/locations.json"

    @staticmethod
    def start():
        with Locations.locations_path.open("r", encoding="utf-8") as f:
            Locations.dictionary = json.load(f)

    @staticmethod
    def get_by_id(id):
        return Locations.dictionary[str(id)]