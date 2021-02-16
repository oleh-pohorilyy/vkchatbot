from Locations import Locations
from Users import Users
import re

def invoke(ctx):
    ctx.reply("", Locations.get_map())