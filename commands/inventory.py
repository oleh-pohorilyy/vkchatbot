from Users import Users
from Inventory import Inventory

def invoke(ctx):
    text = ctx.message["text"].split()
    if len(text) == 1: show(ctx)
    elif len(text) == 3: remove(text, ctx)


def show(ctx):
    msg_text = "Ваш инвентарь: \n"
    user = Users.get_by_id(ctx.message["from_id"])
    print(user["inventory"])
    print(Users.items)
    if user["inventory"]:
        i = 1
        for item in user["inventory"]:
            msg_text += str(i) + ". " + Users.items[str(item)]["name"] + "\n"
            i += 1
        ctx.reply(msg_text)
    else:
        ctx.reply("Ваш инвентарь пуст!")

def remove(text, ctx):
    user = Users.get_by_id(ctx.message["from_id"])
    if text[1].lower() == "выкинуть":
        try:
            if int(text[2]) <= 0: raise Exception()
            ctx.reply("Вы выбросили {}".format(Users.items[str(user["inventory"][int(text[2]) - 1])]["name"]))
            Inventory.remove(user["inventory"][int(text[2])-1], ctx.message["from_id"])
        except Exception:
            ctx.reply("Предмет не найден.")
