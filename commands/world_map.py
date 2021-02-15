from Locations import Locations
from Users import Users
from Assets import Assets
import re

def invoke(ctx):
    ctx.reply("", Assets.dictionary["world_map.jpg"]["remote"])