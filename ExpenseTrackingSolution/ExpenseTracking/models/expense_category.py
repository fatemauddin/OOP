class ExpenseCategory:
    def __init__(self, category_id, name, is_active=True):
        self.category_id = category_id
        self.name = name
        self.is_active = is_active

    def __str__(self):
        status = "Active" if self.is_active else "Inactive"
        return f"{self.category_id} - {self.name} ({status})"
