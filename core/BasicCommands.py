from Users import Users

class Commands:

    @staticmethod
    def profile(ctx):
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

    @staticmethod
    def change_nickname(ctx):
        newname = ""
        user = Users.get_by_id(ctx.message["from_id"])
        try:
            newname = ctx.message["text"].split()[1]
            ctx.reply("Ник успешно изменен.")
        except:
            ctx.reply("Указан недопустимый ник!")
        Users.change_value(ctx.message["from_id"], "name", newname)