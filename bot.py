import sys
import json
sys.path.append("core/")
from VK import LongPoll

with open("config.json") as f:
    config = json.load(f)

bot = LongPoll(config["token"], config["group_id"])

bot.command("(?i)^тест", lambda ctx: ctx["reply"]("DAROVA"))

bot.start()