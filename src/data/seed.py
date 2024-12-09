import sqlite3 
from src.data.db_connection import get_connection

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
    query = 'INSERT INTO products (code, name, price, stock) VALUES (?, ?, ?, ?)'
    conn = get_connection()
    cursor = conn.cursor()
    try:        
        cursor.execute('SELECT COUNT(*) FROM products')
        product_count = cursor.fetchone()[0]
        if product_count == 0:
            # Si la base de datos está vacía, insertar todos los productos
            cursor.executemany(query, new_products)
            conn.commit()            

    except sqlite3.Error as e:
        print(f'Error al interactuar con la base de datos: {e}')
    finally:    
        if conn:
            conn.close()