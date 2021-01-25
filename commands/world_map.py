from Locations import Locations
from Users import Users
import re

def invoke(ctx):
    ctx.reply("", Users.get_by_id(ctx.message["from_id"])["media"]["world_map"])