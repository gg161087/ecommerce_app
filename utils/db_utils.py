import sqlite3

def connect_to_db():
    return sqlite3.connect('data/ecommerce.db')

def create_tables(conn):
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        price REAL NOT NULL)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS customers (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        email TEXT NOT NULL UNIQUE)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS orders (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        customer_id INTEGER,
                        total REAL,
                        FOREIGN KEY(customer_id) REFERENCES customers(id))''')

    conn.commit()
