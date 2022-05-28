import sqlite3

def Database():
    global conn, cursor
    # Connect database
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()
    # Query create table
    cursor.execute("CREATE TABLE IF NOT EXISTS 'user' (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, password TEXT)")
