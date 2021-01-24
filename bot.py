import sys
import json
sys.path.append("core/")
sys.path.append("commands/")
from Users import Users
from Items import Items
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

Items.start() # Loading items
Users.start() # Loading users, running autosave, checking for new user structure 
bot.start()