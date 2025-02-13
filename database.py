import sqlite3


class Database:
    def __init__(self, path):
        self.path = path

    def create_tables(self):
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS reviews(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    contact TEXT,
                    rate INTEGER,
                    text TEXT
                )        
            """)
            conn.commit()

    def add_review(self, data: dict):
        print(data)
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO reviews (name, contact, rate, text) VALUES (?, ?, ?, ?)
            """,
                (data["name"], data["contact"], data["rate"], data["text"]),
            )
            conn.commit()