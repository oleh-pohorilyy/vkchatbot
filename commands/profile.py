def invoke(ctx):
    fancy = {"name": "💬 Ник",
                "bot_id": "⚙ Айди у бота",
                "balance": "💶 Баланс"
                }
    msg_text = ""
    user = Users.get_by_id(ctx.message["from_id"])
    for key in user:
        if key in ["id"]:
            continue
        try:
            msg_text += fancy[key] + ": " + str(user[key]) + "\n"
        except:
            msg_text += key + ": " + str(user[key]) + "\n"
    ctx.reply(msg_text)