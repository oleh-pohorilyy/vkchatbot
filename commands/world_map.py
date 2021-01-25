from Locations import Locations
import re

def invoke(ctx):
    map_path = Locations.get_map()
    ctx.reply("", str(map_path))