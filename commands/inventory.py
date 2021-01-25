from Users import Users
from Inventory import Inventory
from Items import Items
import re
from utils import u_map


def invoke(ctx):
    text = ctx.message["text"]
    drop_info = re.search("(?i)выкинуть \d+", text)
    sort_info = re.search("(?i)сорт", text)
    if drop_info is not None:
        drop(ctx, drop_info.group())
    elif sort_info is not None:
        sort(ctx)
    else:
        show(ctx)


def show(ctx):
    try:
        user = Users.get_by_id(ctx.message["from_id"])
        fancy = {"consumable": "🧪",
                "weapon": "🗡",
                "armor": "🛡",
                "accessory1": "💍",
                "accessory2": "💍"
                }
                
        if not user["inventory"]: raise Exception("Ваш инвентарь пуст!")

        items = u_map(lambda id, _: Items.get_by_id(id), user["inventory"])
        item_list_string = u_map(lambda item, i: f'〔 {i+1} 〕~{fancy[item["type"]]}~ {item["name"]}', items)

        formatted_text = "-~ໂƸ~⌘~Ʒໃ-~⫷x⫸-~ໂƸ~⌘~Ʒໃ-➵\n::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: : : : :\n"+"\n".join(item_list_string)+"\n::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: : : : :\n-~ໂƸ~⌘~Ʒໃ-~⫷o⫸-~ໂƸ~⌘~Ʒໃ-➵"

        ctx.reply(formatted_text)
    except Exception as e:
        ctx.reply(e)


def drop(ctx, drop_info):
    try:
        user = Users.get_by_id(ctx.message["from_id"])
        drop_index = int(re.search("\d+", drop_info).group())-1

        if drop_index < 0 or drop_index >= len(user["inventory"]):
            raise Exception("Предмет не найден!")

        item_id = user["inventory"][drop_index]
        item_data = Items.get_by_id(item_id)
        Inventory.remove(item_id, ctx.message["from_id"])

        ctx.reply(f'Вы выбросили "{item_data["name"]}"')
    except Exception as e:
        ctx.reply(e)


def sort(ctx):
    Inventory.sort(ctx.message["from_id"])
    show(ctx)
