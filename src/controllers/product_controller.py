from src.utils.displayer import display_divider, display_products, display_product_requirements, display_back_menu, display_table_headers, display_product
from src.utils.validate_inputs import validate_back, validated_input, validate_code, validate_name, validate_price, validate_stock
from src.services.product_service import (
    add_product,
    get_all_products,
    search_product,
    update_product,
    delete_product,
    get_low_stock_products,
)

def create_product_controller():
    display_product_requirements()

    code = validated_input("Ingrese el código del producto (mín. 4 dígitos): ", "", validate_code)
    if code == 'v': return

    name = validated_input("Ingrese el nombre del producto: ", "", validate_name)
    if name == 'v': return

    price = validated_input("Ingrese el precio del producto: ", "", validate_price)
    if price == 'v': return

    stock = validated_input("Ingrese el stock inicial: ", "", validate_stock)
    if stock == 'v': return

    add_product(int(code), name, float(price), int(stock))
    print("Producto agregado exitosamente.")

def list_products_controller():
    products = get_all_products()
    if products:
        display_products(products)
    else:
        print("No hay productos disponibles.")

def retrieve_product_by_id():
    display_back_menu() 
    back = False
    while not back:
        prompt = input('\t Ingrese el ID del producto: ')            
        if not validate_back(prompt) and (back := True):
            break
        else:
            if prompt.isnumeric() and int(prompt) > 0:
                product_id = int(prompt)
                product = search_product('id', product_id)
                if product:
                    display_table_headers()
                    display_product(product)
                    display_divider()                    
                else:
                    print(f'No se encontró un producto con ID {product_id}.')
            else:
                print('El ID del producto debe ser numerico y mayor que 0.')

def retrieve_product_by_code():
    display_back_menu() 
    back = False
    while not back:
        prompt = input('\t Ingrese el CÓDIGO del producto: ')            
        if not validate_back(prompt) and (back := True):
            break
        else:
            if validate_code(prompt):
                code = int(prompt)
                product = search_product('code', code)
                if product:
                    display_table_headers()
                    display_product(product)
                    display_divider()                    
                else:
                    print(f'No se encontró un producto con CÓDIGO {code}.')
            else:
                print('El CÓDIGO del producto debe ser numerico y mayor que 0.')

def retrieve_product_by_name():
    display_back_menu() 
    back = False
    while not back:
        prompt = input('\t Ingrese el NOMBRE del producto: ')            
        if not validate_back(prompt) and (back := True):
            break
        else:
            if validate_name(prompt):
                name = prompt.capitalize()
                product = search_product('name', name)
                if product:
                    display_table_headers()
                    display_product(product)
                    display_divider()                    
                else:
                    print(f'No se encontró un producto con NOMBRE {name}.')
            else:
                print('El NOMBRE del producto debe tener al menos 3 caracteres.')


def search_product_controller(condition):
    if condition == 'id':
        retrieve_product_by_id()
    elif condition == 'code':
        retrieve_product_by_code()
    else:
        retrieve_product_by_name()

def update_product_controller():
    product_id = input("Ingrese el ID del producto a actualizar: ").strip()
    product = search_product('1', product_id)

    if not product:
        print("Producto no encontrado.")
        return

    print("Actualizando producto:")
    print(product)

    new_code = validated_input("Nuevo código: ", product['code'], validate_code)
    new_name = validated_input("Nuevo nombre: ", product['name'], validate_name)
    new_price = validated_input("Nuevo precio: ", product['price'], validate_price)
    new_stock = validated_input("Nuevo stock: ", product['stock'], validate_stock)

    if update_product(int(product_id), int(new_code), new_name, float(new_price), int(new_stock)):
        print("Producto actualizado correctamente.")
    else:
        print("Error al actualizar el producto.")

def delete_product_controller():
    product_id = input("Ingrese el ID del producto a eliminar: ").strip()
    if delete_product(int(product_id)):
        print("Producto eliminado correctamente.")
    else:
        print("Producto no encontrado.")

def low_stock_report_controller():
    products = get_low_stock_products()
    if products:
        print("Productos con stock bajo:")
        display_products(products)
    else:
        print("No hay productos con stock bajo.")
