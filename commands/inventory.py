from Users import Users
from Inventory import Inventory
from Items import Items
import re


def invoke(ctx):
    text = ctx.message["text"]
    drop_info = re.search("(?i)выкинуть \d+", text)
    sort_info = re.search("(?i)сортировать", text)
    if drop_info is not None:
        drop(ctx, drop_info.group())
    elif sort_info is not None:
        sort(ctx)
    else:
        show(ctx)


def show(ctx):
    user = Users.get_by_id(ctx.message["from_id"])
    fancy = {"consumable": "🧪",
             "weapon": "🗡",
             "armor": "🛡",
             "accessory1": "💍",
             "accessory2": "💍"
             }
    if user["inventory"]:
        mapped_items = list(map(lambda item_id: "~" + fancy[Items.get_by_id(item_id)["type"]] + "~ " + Items.get_by_id(item_id)["name"], user["inventory"]))
        numbers = range(1, len(mapped_items)+1)
        items_with_numbers = list(map(lambda item, number: "〔 " + str(number)+' 〕'+item, mapped_items, numbers))
        formatted_text = "-~ໂƸ~⌘~Ʒໃ-~⫷x⫸-~ໂƸ~⌘~Ʒໃ-➵\n::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: : : : :\n" + "\n".join(items_with_numbers) + "\n::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: : : : :\n-~ໂƸ~⌘~Ʒໃ-~⫷o⫸-~ໂƸ~⌘~Ʒໃ-➵"

        ctx.reply(formatted_text)
    else:
        ctx.reply("Ваш инвентарь пуст!")


def drop(ctx, drop_info):
    user = Users.get_by_id(ctx.message["from_id"])
    drop_index = int(re.search("\d+", drop_info).group())-1

    try:
        if drop_index <= 0:
            raise Exception()

        item_id = user["inventory"][drop_index]
        item_data = Items.get_by_id(item_id)
        is_removed = Inventory.remove(item_id, ctx.message["from_id"])

        if not is_removed:
            raise Exception()
        ctx.reply(f'Вы выбросили "{item_data["name"]}"')
    except:
        ctx.reply("Предмет не найден.")


def sort(ctx):
    Inventory.sort(ctx.message["from_id"])
    show(ctx)
