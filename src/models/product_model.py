import sqlite3 
from src.data.db_connection import get_connection

def insert_product(code, name, price, stock, table_name):
    query = f"""
        INSERT INTO {table_name} (code, name, price, stock) VALUES (?, ?, ?, ?)
    """    
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(query, (code, name, price, stock))
        conn.commit()                    
        return True
    except sqlite3.IntegrityError as e:
        print(f'Error: El código: {code}, ya existe. Detalles: {e}')
        return None
    finally:
        if conn:  # Verifica si `conn` fue inicializado
            conn.close()

def fetch_all_products(table_name):
    query = f'SELECT * FROM {table_name}'   
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        conn.close()
        keys = ['id', 'code', 'name', 'price', 'stock']
        dict_results = [dict(zip(keys, row)) for row in results]
        return dict_results
    except sqlite3.Error as e:  # Manejar errores de SQLite
        print(f'Error al obtener los productos: {e}')
        return None
    finally:
        if conn:  # Verifica si `conn` fue inicializado
            conn.close()   

def fetch_product_dynamic(condition, parameter):
    query = f'SELECT * FROM products WHERE {condition} = ?'
    conn = get_connection()
    cursor = conn.cursor()
    try:
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
    except sqlite3.Error as e:  # Manejar errores de SQLite
        print(f'Error al obtener el producto: {e}')
        return None    
    finally:
        if 'conn' in locals():  # Verifica si `conn` fue inicializado
            conn.close()

def update_product_by_id(product_id, code, name, price, stock):
    query = """
        UPDATE products
        SET code = ?, name = ?, price = ?, stock = ?
        WHERE id = ?
    """
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(query, (code, name, price, stock, product_id))
        conn.commit()
        updated_rows = cursor.rowcount
        conn.close()
        return updated_rows > 0
    except sqlite3.Error as e:  # Manejar errores de SQLite
        print(f'Error al actualizar el producto con ID {product_id}: {e}')
        return False  # Devuelve `False` en caso de error
    finally:
        if 'conn' in locals():  # Verifica si `conn` fue inicializado
            conn.close()   

def delete_product_by_id(product_id):
    query_check = 'SELECT 1 FROM products WHERE id = ?'
    query_delete = 'DELETE FROM products WHERE id = ?'
    conn = get_connection()
    cursor = conn.cursor()
    try:
        # Verificar si el producto existe
        cursor.execute(query_check, (product_id,))
        product_exists = cursor.fetchone()
        if product_exists:
            # El producto existe, proceder con la eliminación
            cursor.execute(query_delete, (product_id,))
            conn.commit()
            return True  # Indica que se eliminó exitosamente
        else:
            # El producto no existe
            return False  # Indica que no se encontró el producto
    except sqlite3.Error as e:
        print(f'Error al intentar eliminar el producto con ID {product_id}: {e}')
        return False
    finally:
        if 'conn' in locals():  # Asegura que la conexión se cierre si fue creada
            conn.close()
    
def fetch_low_stock_products():
    query = 'SELECT * FROM products WHERE stock <= 10'
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        conn.close()
        keys = ['id', 'code','name', 'price', 'stock']
        dict_results = [dict(zip(keys, row)) for row in results]
        return dict_results
    except sqlite3.Error as e:  # Manejar errores de SQLite
        print(f'Error al obtener los productos con bajo stock: {e}')
        return None
    finally:
        if 'conn' in locals():  # Verifica si `conn` fue inicializado
            conn.close() 