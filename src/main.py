from item import Item
from inventory import Inventory
from report import Report
from filehandler import FileHandler
from user import User

from datetime import datetime

def main():
 
    inventory = Inventory()
    file_handler = FileHandler('inventory_data.json')
    user = User("admin", "admin")


    inventory.items = file_handler.load_inventory()


    if user.login("admin", "admin"):

        new_item = Item(1, 'Lipstick', 'Makeup', 12.99, 10, color='Red', expiration_date=datetime(2024, 12, 31).date())
        inventory.add_item(new_item)

 
        report = Report(inventory)
        low_stock = report.low_stock_report()
        print("Low Stock Report:", low_stock)

      
        file_handler.save_inventory(inventory)

if __name__ == "__main__":
    main()
