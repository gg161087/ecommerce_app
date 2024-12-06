import time
from src.utils.displayer import (
    display_divider, 
    display_products, 
    display_product_requirements, 
    display_back_menu, 
    display_table_headers, 
    display_product, 
    display_confirm,
    clear_screen
)
from src.utils.validate_inputs import (
    validate_back, 
    validate_id, 
    validated_input, 
    validate_code, 
    validate_name, 
    validate_price, 
    validate_stock
)
from src.services.product_service import (
    add_product,
    get_all_products,
    search_product,
    update_product,
    delete_product,
    get_low_stock_products,
)

def create_product_controller():
    display_back_menu()
    display_product_requirements()
    code = validated_input('\tIngrese el código numérico del producto (mín. 4 dígitos): ', '', validate_code, allow_skip=False)
    if code == 'v':
        clear_screen() 
        return

    name = validated_input('\tIngrese el nombre del producto: ', '', validate_name, allow_skip=False)
    if name == 'v': 
        clear_screen()
        return

    price = validated_input('\tIngrese el precio del producto: ', '', validate_price, allow_skip=False)
    if price == 'v':
        clear_screen()
        return

    stock = validated_input('\tIngrese el stock inicial: ', '', validate_stock, allow_skip=False)
    if stock == 'v':
        clear_screen()
        return

    add_product(int(code), name, float(price), int(stock))
    print('Producto agregado exitosamente.')

def list_products_controller():
    products = get_all_products()
    if products:
        display_products(products)
    else:
        print('No hay productos disponibles.')

def retrieve_product_by_id():
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
                    clear_screen()
                    display_back_menu()
                    display_table_headers()
                    display_product(product)
                    display_divider()                    
                else:
                    print(f'No se encontró un producto con ID {product_id}.')
            else:
                print('El ID del producto debe ser numerico y mayor que 0.')

def retrieve_product_by_code():
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
                    clear_screen()
                    display_back_menu()                    
                    display_table_headers()
                    display_product(product)
                    display_divider()                    
                else:
                    print(f'No se encontró un producto con CÓDIGO {code}.')
            else:
                print('El CÓDIGO del producto debe ser numerico y mayor que 0.')

def retrieve_product_by_name():
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
                    clear_screen()
                    display_back_menu()
                    display_table_headers()
                    display_product(product)
                    display_divider()                    
                else:
                    print(f'No se encontró un producto con NOMBRE {name}.')
            else:
                print('El NOMBRE del producto debe tener al menos 3 caracteres.')

def search_product_controller(condition):
    display_back_menu()
    if condition == 'id':
        retrieve_product_by_id()
    elif condition == 'code':
        retrieve_product_by_code()
    else:
        retrieve_product_by_name()

def remove_product_by_id():
    back = False
    confirm = False
    while not back:
        prompt = input('\t Ingrese el ID del producto a eliminar: ').strip()           
        if not validate_back(prompt) and (back := True):
            break
        else:
            if validate_id(prompt):
                product_id = int(prompt)
                product = search_product('id', product_id)
                if product:
                    display_table_headers()
                    display_product(product)
                    display_divider()
                    display_confirm('ELIMINAR')
                    while not confirm:
                        prompt_confirm = input('\t Seleccione una opción: ').strip().lower()
                        if prompt_confirm == 's':
                            if delete_product(int(product['id'])):
                                print('Producto eliminado correctamente.')
                                time.sleep(5)
                                break
                        elif prompt_confirm == 'n':
                            clear_screen()
                            display_back_menu()
                            break                            
                        else:
                            print('Elija una opcion valida.')                                     
                else:
                    print(f'No se encontró un producto con ID {product_id}.')
            else:
                print('El ID del producto debe ser numerico y mayor que 0.')

def remove_product_by_code():
    back = False
    confirm = False
    while not back:
        clear_screen()
        display_back_menu() 
        prompt = input('\t Ingrese el CÓDIGO del producto a eliminar: ').strip()           
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
                    display_confirm('ELIMINAR')
                    while not confirm:
                        prompt_confirm = input('\t Seleccione una opción: ').strip().lower()
                        if prompt_confirm == 's':
                            if delete_product(int(product['id'])):
                                print('Producto eliminado correctamente.')
                                time.sleep(5)
                                break
                        elif prompt_confirm == 'n':
                            clear_screen()
                            display_back_menu()
                            break                            
                        else:
                            print('Elija una opcion valida.')                         
                else:
                    print(f'No se encontró un producto con CÓDIGO {code}.')
            else:
                print('El CÓDIGO del producto debe ser numerico y mayor que 0.')

def remove_product_by_name():
    back = False
    confirm = False
    while not back:
        clear_screen()
        display_back_menu() 
        prompt = input('\t Ingrese el NOMBRE del producto a eliminar: ')            
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
                    display_confirm('ELIMINAR')
                    while not confirm:
                        prompt_confirm = input('\t Seleccione una opción: ').strip().lower()
                        if prompt_confirm == 's':
                            if delete_product(int(product['id'])):
                                print('Producto eliminado correctamente.')
                                time.sleep(5)
                                break
                        elif prompt_confirm == 'n':
                            clear_screen()
                            display_back_menu()
                            break                            
                        else:
                            print('Elija una opcion valida.')                            
                else:
                    print(f'No se encontró un producto con NOMBRE {name}.')
            else:
                print('El NOMBRE del producto debe tener al menos 3 caracteres.')

def remove_product_controller(condition):
    if condition == 'id':
        remove_product_by_id()
    elif condition == 'code':
        remove_product_by_code()
    else:
        remove_product_by_name()

def new_data_product(product):
    confirm = False
    display_table_headers()
    display_product(product)
    display_divider()
    display_product_requirements()
    new_code = validated_input('\tNuevo código(Presione enter para dejar el que estaba): ', product['code'], validate_code)
    if new_code == 'v':
        clear_screen() 
        return
    new_name = validated_input('\tNuevo nombre(Presione enter para dejar el que estaba): ', product['name'], validate_name)
    if new_name == 'v':
        clear_screen()
        return                    
    new_price = validated_input('\tNuevo precio(Presione enter para dejar el que estaba): ', product['price'], validate_price)
    if new_price == 'v':
        clear_screen()
        return
    new_stock = validated_input('\tNuevo stock(Presione enter para dejar el que estaba): ', product['stock'], validate_stock)
    if new_stock == 'v':
        clear_screen()
        return                    
    new_product = {
        'id': product['id'],
        'code': new_code,
        'name': new_name,
        'price': new_price,
        'stock': new_stock
    }
    clear_screen()
    display_table_headers()
    display_product(new_product)
    display_divider()
    display_confirm('ACTUALIZAR')
    while not confirm:
        prompt_confirm = input('\t Seleccione una opción: ').strip().lower()
        if prompt_confirm == 's':
            if update_product(int(product['id']), int(new_code), new_name, float(new_price), int(new_stock)):
                print('Producto actualizado correctamente.')
                time.sleep(5)
                break
        elif prompt_confirm == 'n':
            clear_screen()
            display_back_menu()
            break                            
        else:
            print('Elija una opcion valida.') 

def update_product_by_id():
    clear_screen()
    display_back_menu()
    back = False
    while not back:
        prompt = input('\t Ingrese el ID del producto a Actualizar: ').strip()           
        if not validate_back(prompt) and (back := True):
            break
        else:
            if validate_id(prompt):
                product_id = int(prompt)
                product = search_product('id', product_id)
                if product:
                    new_data_product(product)          
                else:
                    print(f'No se encontró un producto con ID {product_id}.')
            else:
                print('El ID del producto debe ser numerico y mayor que 0.')

def update_product_dynamic(condition):
    condition = condition.upper()
    back = False
    while not back:
        clear_screen()
        display_back_menu()
        prompt = input(f'\t Ingrese el {condition} del producto a Actualizar: ').strip()           
        if not validate_back(prompt) and (back := True):
            break
        else:
            if condition == 'ID':
                if validate_id(prompt):
                    product_id = int(prompt)
                    product = search_product('id', product_id)
                    if product:
                        new_data_product(product)          
                    else:
                        print(f'No se encontró un producto con el ID: {product_id}.')
                else:
                    print('El ID del producto debe ser numerico y mayor que 0.')
            elif condition == 'CODIGO':
                if validate_code(prompt):
                    code = int(prompt)
                    product = search_product('code', code)
                    if product:
                        new_data_product(product)          
                    else:
                        print(f'No se encontró un producto con el CODIGO: {code}.')
            else:
                if validate_name(prompt):                    
                    product = search_product('name', prompt)
                    if product:
                        new_data_product(product)          
                    else:
                        print(f'No se encontró un producto con el NOMBRE: {prompt}.')                                    

def update_product_controller(condition):
    condition = condition.upper()
    if condition == 'ID':
        update_product_dynamic('ID')
    elif condition == 'CODE':
        update_product_dynamic('CODIGO')
    else:
        update_product_dynamic('NOMBRE')

def low_stock_report_controller():
    products = get_low_stock_products()
    if products:
        print('Productos con stock bajo:')
        display_products(products)
    else:
        print('No hay productos con stock bajo.')
