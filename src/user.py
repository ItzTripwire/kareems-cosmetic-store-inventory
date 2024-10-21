class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role  # e.g., 'admin', 'manager'

    def login(self, username, role):
        if username == self.username and role == self.role:
            print(f"User {self.username} logged in as {self.role}.")
            return True
        else:
            print("Invalid credentials!")
            return False

    def get_permissions(self):
        if self.role == "admin":
            return ["add_item", "remove_item", "update_item", "generate_reports"]
        elif self.role == "manager":
            return ["view_inventory", "generate_reports"]
        else:
            return []
