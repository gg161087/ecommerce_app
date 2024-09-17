from models.product_model import create_product, get_products, get_product, update_product, delete_product

def add_product(conn):
    name = input("Nombre del producto: ")
    price = float(input("Precio del producto: "))
    create_product(conn, name, price)
    print(f"Producto '{name}' agregado con éxito.")

def list_products(conn):
    products = get_products(conn)
    if not products:
        print("La lista de productos está vacía.")
    else:
        for product in products:
            print(f"{product[0]} - {product[1]} - ${product[2]:.2f}")

def list_product(conn):
    product_id = int(input("Ingrese el ID del producto: "))
    product = get_product(conn, product_id)
    
    if product:
        print(f"Producto ID: {product['id']}")
        print(f"Nombre: {product['name']}")
        print(f"Precio: ${product['price']:.2f}")
    else:
        print(f"No se encontró un producto con ID {product_id}.")

def modify_product(conn):
    product_id = int(input("Ingrese el ID del producto a actualizar: "))
    new_name = input("Nuevo nombre del producto (presiona Enter para no cambiarlo): ")
    new_price = input("Nuevo precio del producto (presiona Enter para no cambiarlo): ")
    new_price = float(new_price) if new_price else None

    if update_product(conn, product_id, new_name if new_name else None, new_price):
        print("Producto actualizado con éxito.")
    else:
        print(f"No se encontró un producto con ID {product_id}.")

def remove_product(conn):
    product_id = int(input("Ingrese el ID del producto a eliminar: "))    
    if delete_product(conn, product_id):
        print(f"Producto con ID {product_id} eliminado con éxito.")
    else:
        print(f"No se encontró un producto con ID {product_id}.")
