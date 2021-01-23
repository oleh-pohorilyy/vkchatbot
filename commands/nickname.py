from Users import Users
def invoke(ctx):
    newname = ""
    try:
        newname = ctx.message["text"].split()[1]
        ctx.reply("Ник успешно изменен.")
    except:
        ctx.reply("Указан недопустимый ник!")
    Users.change_value(ctx.message["from_id"], "name", newname)