import sqlite3
import os

DB_FILE = "/app/data/database.db"

def get_db_connection():
    os.makedirs(os.path.dirname(DB_FILE), exist_ok=True)
    conn = sqlite3.connect(DB_FILE, check_same_thread=False)
    conn.execute("CREATE TABLE IF NOT EXISTS data (key INTEGER PRIMARY KEY, value TEXT)")
    return conn

def save_data(key: int, value: str):
    with get_db_connection() as conn:
        conn.execute("INSERT OR REPLACE INTO data (key, value) VALUES (?, ?)", (key, value))
        conn.commit()
    return value

def get_data(key: int):
    with get_db_connection() as conn:
        cursor = conn.execute("SELECT value FROM data WHERE key = ?", (key,))
        result = cursor.fetchone()
    return result[0] if result else None
