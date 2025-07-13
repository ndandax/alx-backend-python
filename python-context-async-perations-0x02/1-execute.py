import sqlite3

class ExecuteQuery:
    def __init__(self, query, params):
        self.query = query
        self.params = params
        self.conn = None
        self.cursor = None
        self.result = None

    def __enter__(self):
        self.conn = sqlite3.connect('users.db')  
        self.cursor = self.conn.cursor()

        
        self.cursor.execute(self.query, self.params)
        self.result = self.cursor.fetchall()  
        return self.result

    def __exit__(self, exc_type, exc_val, exc_tb):
    
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()


        if exc_type:
            print(f"An error occurred: {exc_val}")
        return False  

query = "SELECT * FROM users WHERE age > ?"
params = (25,)

with ExecuteQuery(query, params) as results:
    for row in results:
        print(row)
