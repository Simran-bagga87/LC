import sqlite3

conn = sqlite3.connect("compliance.db")
cursor = conn.cursor()

columns = """
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name_of_establishment TEXT,
    type_of_establishment TEXT,
    category_of_employer TEXT,
    business_or_trade_type TEXT,
    manager TEXT,
    date_of_opening TEXT,
    work_start_time TEXT,
    work_end_time TEXT,
    intervals INTEGER,
    slot1 TEXT,
    slot2 TEXT,
    slot3 TEXT,
    slot4 TEXT,
    slot5 TEXT
"""

cursor.execute(f"CREATE TABLE IF NOT EXISTS s_e_karnataka ({columns})")
cursor.execute(f"CREATE TABLE IF NOT EXISTS s_e_mumbai ({columns})")

conn.commit()
conn.close()