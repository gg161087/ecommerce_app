from src.data.db_connection import get_connection

def create_product(name, price, stock):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO products (name, price, stock) VALUES (?, ?, ?)', (name, price, stock))
    conn.commit()
    conn.close()

def get_products():   
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products')
    results = cursor.fetchall()
    conn.close()
    keys = ['id', 'name', 'price', 'stock']
    dict_results = [dict(zip(keys, row)) for row in results]
    return dict_results

def get_product(product_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, name, price, stock
        FROM products
        WHERE id = ?
    """, (product_id,))
    
    row = cursor.fetchone()
    conn.close()
    
    if row:        
        return {
            "id": row[0],
            "name": row[1],
            "price": row[2],
            "stock": row[3],
        }
    return None

def update_product(product_id, name, price, stock):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE products
        SET name = ?, price = ?, stock = ?
        WHERE id = ?
    """, (name, price, stock, product_id))
    conn.commit()
    updated_rows = cursor.rowcount
    conn.close()
    return updated_rows > 0

def delete_product(product_id):
    conn = get_connection()
    cursor = conn.cursor()
    # Verificar si el producto existe
    cursor.execute("SELECT 1 FROM products WHERE id = ?", (product_id,))
    product_exists = cursor.fetchone()
    if product_exists:
        # El producto existe, proceder con la eliminación
        cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
        conn.commit()
        conn.close()
        return True  # Indica que se eliminó exitosamente
    else:
        # El producto no existe
        conn.close()
        return False  # Indica que no se encontró el producto
    
def get_products_low_stock():   
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products WHERE stock <= 10')
    results = cursor.fetchall()
    conn.close()
    keys = ['id', 'name', 'price', 'stock']
    dict_results = [dict(zip(keys, row)) for row in results]
    return dict_results