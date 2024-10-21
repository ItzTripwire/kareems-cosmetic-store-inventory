from datetime import datetime

class Item:
    def __init__(self, item_id, name, category, price, quantity, color=None, size=None, expiration_date=None):
        self.item_id = item_id
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity
        self.color = color
        self.size = size
        self.expiration_date = expiration_date

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity

    def get_details(self):
        return {
            "ID": self.item_id,
            "Name": self.name,
            "Category": self.category,
            "Price": self.price,
            "Quantity": self.quantity,
            "Color": self.color,
            "Size": self.size,
            "Expiration Date": self.expiration_date.strftime('%Y-%m-%d') if self.expiration_date else None
        }
