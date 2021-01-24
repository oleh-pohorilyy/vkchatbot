from Users import Users
from Inventory import Inventory
from Items import Items
import re

def invoke(ctx):
    text = ctx.message["text"]
    drop_info = re.search("(?i)выкинуть \d+", text)
    if drop_info is not None: drop(ctx, drop_info.group())
    else: show(ctx)


def show(ctx):
    user = Users.get_by_id(ctx.message["from_id"])

    if user["inventory"]:
        mapped_items = list(map(lambda item_id: Items.get_by_id(item_id)["name"], user["inventory"]))
        numbers = range(1, len(mapped_items)+1)
        items_with_numbers = list(map(lambda item, number: str(number)+'. '+item, mapped_items, numbers))
        formatted_text = "\n".join(items_with_numbers)

        ctx.reply("Ваш инвентарь: \n"+formatted_text)
    else:
        ctx.reply("Ваш инвентарь пуст!")

def drop(ctx, drop_info):
    user = Users.get_by_id(ctx.message["from_id"])
    drop_index = int(re.search("\d+", drop_info).group())-1

    try:
        if drop_index <= 0: raise Exception()

        item_id = user["inventory"][drop_index]
        item_data = Items.get_by_id(item_id)
        is_removed = Inventory.remove(item_id, ctx.message["from_id"])

        if(is_removed != True): raise Exception()
        ctx.reply(f'Вы выбросили "{item_data["name"]}"')
    except:
        ctx.reply("Предмет не найден.")
