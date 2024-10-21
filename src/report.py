from datetime import datetime

class Report:
    def __init__(self, inventory):
        self.inventory = inventory

    def low_stock_report(self, threshold=5):
        low_stock_items = [item for item in self.inventory.items if item.quantity < threshold]
        return [item.get_details() for item in low_stock_items]

    def expiry_report(self):
        today = datetime.today().date()
        expired_items = [item for item in self.inventory.items if item.expiration_date and item.expiration_date < today]
        return [item.get_details() for item in expired_items]
