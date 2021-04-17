from pathlib import Path
from Assets import Assets
from Users import Users
import json


class Locations:
    dictionary = {}
    map_path = None
    locations_path = Path(__file__).parent / "../database/locations.json"

    @staticmethod
    def start():
        Locations.map_path = Assets.get_resource_remote_path("world_map.jpg")
        with Locations.locations_path.open("r", encoding="utf-8") as f:
            Locations.dictionary = json.load(f)

    @staticmethod
    def travel(user_id, location_id):
        location_info = Users.get_by_id(user_id)["location_info"]
        location_info["id"] = location_id
        location_info["loot"].clear()

    @staticmethod
    def get_by_id(id):
        return Locations.dictionary[str(id)]

    @staticmethod
    def get_map():
        return Locations.map_path
