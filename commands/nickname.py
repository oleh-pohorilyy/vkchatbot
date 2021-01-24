from Users import Users
def invoke(ctx):
    try:
        newname = ctx.message["text"].split()[1]
        ctx.reply("Ник успешно изменен.")
        Users.change_value(ctx.message["from_id"], "name", newname)
    except:
        ctx.reply("Указан недопустимый ник!")
    