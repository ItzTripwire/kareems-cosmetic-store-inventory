import json
from datetime import datetime

class FileHandler:
    def __init__(self, file_path):
        self.file_path = file_path

    def save_inventory(self, inventory):
        data = [item.get_details() for item in inventory.items]
        with open(self.file_path, 'w') as f:
            json.dump(data, f)

    def load_inventory(self):
        try:
            with open(self.file_path, 'r') as f:
                data = json.load(f)
            items = []
            for item_data in data:
                item = Item(
                    item_data['ID'], item_data['Name'], item_data['Category'],
                    item_data['Price'], item_data['Quantity'], item_data['Color'],
                    item_data['Size'], datetime.strptime(item_data['Expiration Date'], '%Y-%m-%d').date() if item_data['Expiration Date'] else None
                )
                items.append(item)
            return items
        except FileNotFoundError:
            return []
