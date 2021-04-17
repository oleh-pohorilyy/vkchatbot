import re
from Locations import Locations

def invoke(ctx):
    location_id = re.search("\d+", ctx.message["text"]).group()
    if not location_id: 
        return

    user_id = ctx.message["from_id"]

    Locations.travel(user_id, location_id)
    location_name = Locations.get_by_id(location_id)["name"]
    ctx.reply(f"Вы телепортировались в {location_name}")
