import pyodbc

class Database:
    def __init__(self):
        self.connection_string = (
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=localhost\\SQLEXPRESS;"
            "DATABASE=expense_tracing_budget_control;"
            "Trusted_Connection=yes;"
        )

    def connect(self):
        return pyodbc.connect(self.connection_string)
