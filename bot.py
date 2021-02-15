import sys
import json
sys.path.append("core/")
sys.path.append("commands/")
from Users import Users
from Items import Items
from Locations import Locations
from Mobs import Mobs
from Assets import Assets
from commands import *
from VK import LongPoll

with open("config.json") as f:
    config = json.load(f)

bot = LongPoll(
    config["token"], 
    config["group_id"], 
    { "use_proxy": config["use_proxy"], "ip": config["proxy_ip"] }
)


bot.command("(?i)^профиль$", profile.invoke)
bot.command("(?i)^ник \w+", nickname.invoke)
bot.command("(?i)(^инвентарь$)|(^инвентарь выкинуть \d+)|(^инвентарь сортировать$)|(^инвентарь сорт$)", inventory.invoke)
bot.command("(?i)^карта$", world_map.invoke)
bot.command("(?i)^перейти \d+", travel.invoke)


Assets.start(bot.upload_photo) # Loading assets
Items.start() # Loading items
Locations.start() # Loading locations
Mobs.start() # Loading mobs
Users.start() # Loading users, running autosave, checking for new user structure 
bot.start()