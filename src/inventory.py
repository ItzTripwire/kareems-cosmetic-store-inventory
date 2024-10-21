class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item_id):
        self.items = [item for item in self.items if item.item_id != item_id]

    def update_item(self, item_id, new_quantity):
        item = self.get_item(item_id)
        if item:
            item.update_quantity(new_quantity)

    def get_item(self, item_id):
        for item in self.items:
            if item.item_id == item_id:
                return item
        return None

    def list_items(self):
        return [item.get_details() for item in self.items]
