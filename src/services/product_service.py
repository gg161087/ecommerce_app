from src.utils.validate_inputs import validate_code, validate_name, validate_price, validate_stock, validated_input, validate_back
from src.models.product_model import create_product, get_products, get_product_dynamic, update_product, delete_product, get_products_low_stock
from src.utils.messages import display_product, display_products, display_table_headers, display_back_menu, display_product_requirements, display_divider

def add_product():
    display_back_menu()
    display_product_requirements()
    back = False
    name = ''
    code = 0
    stock = 0
    price = 0

    while not back:
        try:
            # Obtener nombre del producto
            name = validated_input('\t Nombre del producto: ', name, validate_name, allow_skip=False)
            if not validate_back(name) and (back := True):                
                break
            # Obtener codigo del producto
            code = validated_input('\t Codigo del producto: ', code, validate_code, allow_skip=False)
            if not validate_back(code) and (back := True):                
                break
            # Obtener precio del producto
            price = validated_input(f'\t Precio de {name}: ', price, validate_price)
            if not validate_back(price) and (back := True):
                break
            price = float(price)
            # Obtener stock del producto
            stock = validated_input(f'\t Stock de {name}: ', stock, validate_stock)
            if not validate_back(stock) and (back := True):
                break
            stock = int(stock)
            # Crear el producto si no se vuelve
            if not back:                
                create_product(code, name, price, stock)
                print(f'Producto "{name}" agregado con éxito.')
                back = True
        except ValueError as ve:
            print(f'Error en la conversión de datos: {ve}')
        except Exception as e:
            print(f'Ocurrió un error inesperado: {e}')

def list_products():
    products = get_products()
    if not products:
        print('La lista de productos está vacía.')
    else:
        display_products(products)

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
                product = get_product_dynamic('id', product_id)
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
                product = get_product_dynamic('code', code)
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
                name = prompt
                product = get_product_dynamic('name', name)
                if product:
                    display_table_headers()
                    display_product(product)
                    display_divider()                    
                else:
                    print(f'No se encontró un producto con NOMBRE {name}.')
            else:
                print('El NOMBRE del producto debe tener al menos 3 caracteres.')

def edit_product():
    display_back_menu()
    back = False
    product_id = 0
    product = {}

    while not back:
        try:
            # Obtener ID del producto
            prompt = validated_input('\t Ingrese el ID del producto a actualizar: ', '', allow_skip=False)
            if not validate_back(prompt):
                return  # Salir si se desea volver al menú anterior
            elif prompt.isnumeric() and int(prompt) > 0:
                product_id = int(prompt)
                product = get_product_dynamic('id', product_id)  # Suponiendo que esta función obtiene el producto
                if not product:
                    print(f'No se encontró un producto con ID {product_id}.')
                    continue
                display_product_requirements()
                display_table_headers()
                display_product(product)
                #print(product)  # Mostrar el producto actual
            else:
                print('El ID del producto debe ser numérico y mayor que 0.')
                continue  # Volver al inicio del bucle
            # Obtener nuevo nombre
            display_divider()
            new_name = validated_input('\t (presiona Enter para no cambiarlo)\n\t Nuevo nombre del producto: ', product['name'], validate_name)
            if not validate_back(new_name) and (back := True):                
                break
            # Obtener nuevo code
            new_code = validated_input(f'\t (presiona Enter para no cambiarlo)\n\t Nuevo code del producto{product['name']}: ', str(product['code']), validate_code)
            if not validate_back(new_code) and (back := True):                
                break
            # Obtener nuevo precio
            new_price_str = validated_input(f'\t (presiona Enter para no cambiarlo)\n\t Nuevo precio del producto {product['name']}: ', str(product['price']), validate_price)
            if not validate_back(new_price_str) and (back := True):
                break
            new_price = float(new_price_str) if new_price_str else product['price']  # Usar el valor actual si se presiona Enter
            # Obtener nuevo stock
            new_stock_str = validated_input(f'\t (presiona Enter para no cambiarlo)\n\t Nuevo stock del producto {product['name']}: ', str(product['stock']), validate_stock)
            if not validate_back(new_stock_str) and (back := True):
                break
            new_stock = int(new_stock_str) if new_stock_str else product['stock']  # Usar el valor actual si se presiona Enter
            # Actualizar producto
            if update_product(product_id, new_code, new_name, new_price, new_stock):
                display_divider()
                print('Producto actualizado con éxito.')
                display_divider()
            else:
                print(f'No se pudo actualizar el producto con ID {product_id}.')
            
            back = True  # Salir del bucle después de la actualización
        except ValueError as ve:
            print(f'Error en la conversión de datos: {ve}')
        except Exception as e:
            print(f'Ocurrió un error inesperado: {e}')

def delete_product_by_id():
    display_back_menu()
    back = False
    while not back:        
        prompt = input('\t Ingrese el número de ID del producto a eliminar: ')
        if not validate_back(prompt) and (back := True):
            break 
        else:
            if prompt.isnumeric() and int(prompt) > 0:
                product_id = int(prompt)      
                if delete_product(product_id):
                    display_divider()
                    print(f'Producto con ID {product_id} eliminado con éxito.')
                    display_divider()
                else:
                    display_divider()
                    print(f'No se encontró un producto con ID {product_id}.')
                    display_divider()
            else:
                display_divider()
                print('El ID tiene que ser numerico y mayor que 0.')
                display_divider()

def low_stock_report():
    products = get_products_low_stock()
    if not products:
        print('La lista de productos está vacía.')
    else:
        display_products(products)