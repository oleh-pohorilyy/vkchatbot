import sys
import json
sys.path.append("core/")
sys.path.append("commands/")
from Users import Users
from commands import *
from VK import LongPoll

with open("config.json") as f:
    config = json.load(f)


bot = LongPoll(config["token"], config["group_id"], config["use_proxy"])

bot.command("(?i)^тест ", lambda ctx: ctx.reply('success!'))
bot.command("(?i)^профиль", profile.invoke)
bot.command("(?i)^ник ", nickname.invoke)
bot.command("(?i)^хуй ", lambda ctx: ctx.reply("ГЕРМАН БРУЕВ ВОПРОС"))

Users.start()
bot.start()