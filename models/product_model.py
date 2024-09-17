import sqlite3

def create_product(conn, name, price):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO products (name, price) VALUES (?, ?)", (name, price))
    conn.commit()

def get_products(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    return cursor.fetchall()

def get_product(conn, product_id):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products WHERE id = ?", (product_id,))
    product = cursor.fetchone()
    if product:        
        return {
            "id": product[0],
            "name": product[1],
            "price": product[2]
        }
    else:
        return None

def update_product(conn, product_id, new_name=None, new_price=None):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products WHERE id = ?", (product_id,))
    product = cursor.fetchone()    
    if not product:
        return False
    if new_name and new_price:
        cursor.execute("UPDATE products SET name = ?, price = ? WHERE id = ?", (new_name, new_price, product_id))
    elif new_name:
        cursor.execute("UPDATE products SET name = ? WHERE id = ?", (new_name, product_id))
    elif new_price:
        cursor.execute("UPDATE products SET price = ? WHERE id = ?", (new_price, product_id))    
    conn.commit()
    return True

def delete_product(conn, product_id):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products WHERE id = ?", (product_id,))
    product = cursor.fetchone()    
    if not product:
        return False
    cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
    conn.commit()
    return True