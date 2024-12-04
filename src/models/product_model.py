from src.data.db_connection import get_connection

def create_product(code, name, price, stock):
    query = """
        INSERT INTO products (code, name, price, stock) VALUES (?, ?, ?, ?)
    """    
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query, (code, name, price, stock))
    conn.commit()
    conn.close()

def get_products():
    query = 'SELECT * FROM products'   
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    keys = ['id', 'code', 'name', 'price', 'stock']
    dict_results = [dict(zip(keys, row)) for row in results]
    return dict_results

def get_product_dynamic(condition, parameter):
    query = f'SELECT * FROM products WHERE {condition} = ?'
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query, (parameter,))    
    row = cursor.fetchone()
    conn.close()    
    if row:        
        return {
            "id": row[0],
            "code": row[1],
            "name": row[2],
            "price": row[3],
            "stock": row[4],
        }
    return None

def update_product(product_id, code, name, price, stock):
    query = """
        UPDATE products
        SET code = ?, name = ?, price = ?, stock = ?
        WHERE id = ?
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query, (code, name, price, stock, product_id))
    conn.commit()
    updated_rows = cursor.rowcount
    conn.close()
    return updated_rows > 0

def delete_product(product_id):
    query = 'SELECT 1 FROM products WHERE id = ?'
    conn = get_connection()
    cursor = conn.cursor()
    # Verificar si el producto existe
    cursor.execute(query, (product_id,))
    product_exists = cursor.fetchone()
    if product_exists:
        # El producto existe, proceder con la eliminación
        cursor.execute('DELETE FROM products WHERE id = ?', (product_id,))
        conn.commit()
        conn.close()
        return True  # Indica que se eliminó exitosamente
    else:
        # El producto no existe
        conn.close()
        return False  # Indica que no se encontró el producto
    
def get_products_low_stock():   
    query = 'SELECT * FROM products WHERE stock <= 10'
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    keys = ['id', 'code','name', 'price', 'stock']
    dict_results = [dict(zip(keys, row)) for row in results]
    return dict_results