from database.db_connection import Database
from models.expense_category import ExpenseCategory

class CategoryService:
    def __init__(self):
        self.db = Database()

    def create_category(self, name):
        query = "INSERT INTO ExpenseCategory (CategoryName) VALUES (?)"
        with self.db.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(query, name)
            conn.commit()

    #def get_categories(self):
        #query = "SELECT CategoryId, CategoryName, IsActive FROM ExpenseCategory"
        #with self.db.connect() as conn:
            #cursor = conn.cursor()
            #rows = cursor.fetchall()
            #return [ExpenseCategory(*row) for row in rows]
    def get_categories(self):
        select_query = "SELECT CategoryId, CategoryName, IsActive FROM ExpenseCategory"

        with self.db.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(select_query)     # ✅ must be called
            rows = cursor.fetchall()  # ✅ safe now

        categories = []
        for row in rows:
            categories.append(
                ExpenseCategory(
                    category_id=row[0],
                    name=row[1],
                    is_active=row[2]
                )
            )
        return categories

