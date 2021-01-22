import sys
import json
sys.path.append("core/")
from BasicCommands import Commands
from Users import Users
from VK import LongPoll

with open("config.json") as f:
    config = json.load(f)


bot = LongPoll(config["token"], config["group_id"])

bot.command("(?i)^тест", lambda ctx: ctx.reply('success!'))
bot.command("(?i)^профиль", Commands.profile)
bot.command("(?i)^ник", Commands.change_nickname)


Users.load_users()
Users.change_users_template()
bot.start()
