from Users import Users
from Items import Items


class Inventory:

    @staticmethod
    def add(item_id, user_id):
        user = Users.get_by_id(user_id)
        if user["max_inv_size"] >= len(user["inventory"]):
            user["inventory"].append(item_id)
            return True
        return False

    @staticmethod
    def remove(item_id, user_id):
        user = Users.get_by_id(user_id)
        if item_id in user["inventory"]:
            user["inventory"].remove(item_id)

    @staticmethod
    def sort(user_id):
        user = Users.get_by_id(user_id)
        user["inventory"].sort()
