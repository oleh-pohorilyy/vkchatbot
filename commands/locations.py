from Locations import Locations

def invoke(ctx):
    message_text = ""
    for id in Locations.dictionary:
        message_text += "{ " + id + " } " + Locations.dictionary[id]["name"] + "\n"
    ctx.reply("Доступные локации:\n\n" + message_text)

    