import sqlite3 
from src.data.db_connection import get_connection
from src.models.product_model import fetch_product_dynamic

new_products = [
    (1001, 'Fideos', 2400.50, 120),
    (1002, 'Arroz', 1200, 100),
    (1003, 'Polenta', 900.50, 110),
    (1004, 'Hamburguesas', 3000, 8),
    (1005, 'Salchicas', 2900.50, 7),
    (1006, 'Atum', 1500, 50),
    (1007, 'Aceitunas', 500.50, 10),
    (1008, 'Leche', 1900, 9),
    (1009, 'Dulce de Leche', 2500.50, 9),
    (1010, 'Shampoo', 2500.50, 80),
    (1011, 'Gelletitas', 2500.50, 50),
    (1012, 'Pan', 2500.50, 10),
    (1013, 'Huevos', 2500.50, 6),
    (1014, 'Mayonesa', 2500.50, 30),
    (1015, 'Mostaza', 2500.50, 20)
]

def seeder():
    product = fetch_product_dynamic('code', 1001)
    if not product:
        query = 'INSERT INTO products (code, name, price, stock) VALUES (?, ?, ?, ?)'
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.executemany(query, new_products)
            conn.commit()
        except sqlite3.OperationalError:
            print('Ocurrio un error al crear los productos.')
        finally:
            conn.close()