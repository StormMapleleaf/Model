import sqlite3

def create_table():
    conn = sqlite3.connect('usage_records.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS equipment_usage (
                        id INTEGER PRIMARY KEY,
                        date TEXT,
                        class TEXT,
                        name TEXT,
                        time TEXT,
                        content TEXT)''')
    conn.commit()
    conn.close()

create_table()
