from Users import Users
def invoke(ctx):
    msg_text = ""
    if ctx.message["from_id"] == 142475797 or ctx.message["from_id"] == 104532380:
        msg_text += "💎💎💎РАЗРАБОТЧИК БОТА💎💎💎\n"
    fancy = {"name": "💬 Ник: ",
                "bot_id": "⚙ Айди у бота: ",
                "balance": "🌕 Золотых: ",
                "weapon": "🗡 Оружие: ",
                "armor": "🛡 Броня: ",
                "level": "🧿 Уровень: ",
                "health": "❤ Здоровье: ",
                "space": "",
                "space2": ""
                }
    user = Users.get_by_id(ctx.message["from_id"])
    for key in user:
        if key in ["id"]:
            continue
        try:
            msg_text += fancy[key] + str(user[key]) + "\n"
        except:
            msg_text += key + ": " + str(user[key]) + "\n"
    ctx.reply(msg_text)