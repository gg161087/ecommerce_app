import time
from src.utils.displayer import (
    display_divider, 
    display_products, 
    display_product_requirements, 
    display_back_menu, 
    display_table_headers, 
    display_product, 
    display_confirm,
    clear_screen,
    display_not_found,
    display_invalid_option,
    display_remove_message,
    display_title_menu,
    display_invalid_id,
    display_invalid_code,
    display_invalid_name
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
    add_product_removed,
    get_all_products_removed
)

def create_product_controller():    
    while True:
        display_title_menu('Agregar Producto', 'V', 'letra')
        display_back_menu()
        display_product_requirements()
        code = validated_input('\tIngrese el código numérico del producto (mín. 4 dígitos): ', '', validate_code, allow_skip=False)
        if code.lower() == 'v':
            clear_screen() 
            break
        display_divider()
        name = validated_input('\tIngrese el nombre del producto: ', '', validate_name, allow_skip=False)
        if name.lower() == 'v': 
            clear_screen()
            break
        display_divider()
        price = validated_input('\tIngrese el precio del producto: ', '', validate_price, allow_skip=False)
        if price.lower() == 'v':
            clear_screen()
            break
        display_divider()
        stock = validated_input('\tIngrese el stock inicial: ', '', validate_stock, allow_skip=False)
        if stock.lower() == 'v':
            clear_screen()
            break
        display_divider()        
        if code and name and price and stock:
            if add_product(int(code), name, float(price), int(stock)):
                clear_screen()
                display_divider()
                print(f'Producto "{name}" agregado con éxito.')
                display_divider()
                product = search_product('name', name)
                if product:
                    display_table_headers()
                    display_product(product)
                    break

def list_products_controller():
    products = get_all_products('products')
    if products:
        display_products(products, 'LISTADO de PRODUCTOS')
    else:
        display_not_found('Productos')        
        time.sleep(3)

def list_products_removed():
    products = get_all_products_removed()
    if products:                
        display_products(products, 'REPORTE de Productos ELIMINADOS')
    else:
        display_not_found('Productos Eliminados') 
        time.sleep(3)

def search_product_dynamic(condition):
    display_title_menu(f'Buscador por {condition}', 'V', 'letra')
    display_back_menu()
    condition = condition.upper()
    back = False
    while not back:
        prompt = input(f'\t Ingrese el {condition} del producto a BUSCAR: ').strip()           
        if not validate_back(prompt) and (back := True):
            clear_screen()
            break
        else:
            if condition == 'ID':
                if validate_id(prompt):
                    product_id = int(prompt)
                    product = search_product('id', product_id)
                    if product:
                        clear_screen()
                        display_back_menu()
                        display_table_headers()
                        display_product(product)
                        display_divider()                    
                    else:
                        display_not_found(f'producto con ID: {product_id}')                    
                else:
                    display_invalid_id()
            elif condition == 'CÓDIGO':
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
                        display_not_found(f'producto con CÓDIGO: {code}')
                else:
                    display_invalid_code() 
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
                        display_not_found(f'producto con NOMBRE: {name}')
                else:
                    display_invalid_name()

def search_product_controller(condition):
    condition = condition.upper()
    if condition == 'ID':
        search_product_dynamic(condition)
    elif condition == 'CÓDIGO':
        search_product_dynamic(condition)
    else:
        search_product_dynamic(condition)

def remove_product_dynamic(condition):
    display_title_menu(f'Eliminar por {condition}', 'V', 'letra')
    display_back_menu()
    condition = condition.upper()
    back = False
    confirm = False
    while not back:
        prompt = input(f'\t Ingrese el {condition} del producto a ELIMINAR: ').strip()           
        if not validate_back(prompt) and (back := True):
            clear_screen()
            break
        else:
            if condition == 'ID':
                if validate_id(prompt):
                    product_id = int(prompt)
                    product = search_product('id', product_id)
                    if product:
                        clear_screen()
                        display_title_menu(f'Eliminar {product['name']}', 'S-N', 'letra')        
                        display_table_headers()
                        display_product(product)
                        display_confirm('ELIMINAR')
                        while not confirm:
                            prompt_confirm = input('\t Seleccione una opción: ').strip().lower()
                            if prompt_confirm == 's':
                                if delete_product(int(product['id'])):
                                    add_product_removed(product['code'], product['name'], product['price'], product['stock'])
                                    display_remove_message()
                                    break
                            elif prompt_confirm == 'n':
                                clear_screen()
                                display_back_menu()
                                break                            
                            else:
                                display_invalid_option()                                                                    
                    else:
                        display_not_found(f'producto con ID: {product_id}')                 
                else:
                    display_invalid_id() 
            elif condition == 'CÓDIGO':
                if validate_code(prompt):
                    code = int(prompt)
                    product = search_product('code', code)
                    if product:
                        clear_screen()
                        display_divider()
                        display_table_headers()
                        display_product(product)
                        display_divider()
                        display_confirm('ELIMINAR')
                        while not confirm:
                            prompt_confirm = input('\t Seleccione una opción: ').strip().lower()
                            if prompt_confirm == 's':
                                if delete_product(int(product['id'])):
                                    add_product_removed(product['code'], product['name'], product['price'], product['stock'])
                                    display_remove_message()
                                    break
                            elif prompt_confirm == 'n':
                                clear_screen()
                                display_back_menu()
                                break                            
                            else:
                                display_invalid_option()                                                    
                    else:
                        display_not_found(f'producto con CÓDIGO: {code}')
                else:
                    display_invalid_code()
            else:
                if validate_name(prompt):
                    name = prompt.capitalize()
                    product = search_product('name', name)
                    if product:
                        clear_screen()
                        display_divider()
                        display_table_headers()
                        display_product(product)
                        display_divider()
                        display_confirm('ELIMINAR')
                        while not confirm:
                            prompt_confirm = input('\t Seleccione una opción: ').strip().lower()
                            if prompt_confirm == 's':
                                if delete_product(int(product['id'])):
                                    add_product_removed(product['code'], product['name'], product['price'], product['stock'])
                                    display_remove_message()
                                    break
                            elif prompt_confirm == 'n':
                                clear_screen()
                                display_back_menu()
                                break                            
                            else:
                                display_invalid_option()                 
                    else:
                        display_not_found(f'producto con NOMBRE {name}')
                else:
                    display_invalid_name()

def remove_product_controller(condition):
    condition = condition.upper()  
    if condition == 'ID':
        remove_product_dynamic(condition)
    elif condition == 'CÓDIGO':
        remove_product_dynamic(condition)
    else:
        remove_product_dynamic(condition)

def new_data_product(product):
    confirm = False
    clear_screen()
    display_back_menu()
    display_table_headers()
    display_product(product)
    display_divider()
    display_product_requirements()
    new_code = validated_input('\tNuevo código(Presione enter para dejar el que estaba): ', product['code'], validate_code)
    if new_code == 'v':
        clear_screen()
        display_back_menu() 
        return
    new_name = validated_input('\tNuevo nombre(Presione enter para dejar el que estaba): ', product['name'], validate_name)
    if new_name == 'v':
        clear_screen()
        display_back_menu()
        return                    
    new_price = validated_input('\tNuevo precio(Presione enter para dejar el que estaba): ', product['price'], validate_price)
    if new_price == 'v':
        clear_screen()
        display_back_menu()
        return
    new_stock = validated_input('\tNuevo stock(Presione enter para dejar el que estaba): ', product['stock'], validate_stock)
    if new_stock == 'v':
        clear_screen()
        display_back_menu()
        return                    
    new_product = {
        'id': product['id'],
        'code': int(new_code),
        'name': new_name,
        'price': float(new_price),
        'stock': int(new_stock)
    }
    clear_screen()
    display_divider()
    display_table_headers()
    display_product(new_product)
    display_divider()
    display_confirm('ACTUALIZAR')
    while not confirm:
        prompt_confirm = input('\t Seleccione una opción: ').strip().lower()
        if prompt_confirm == 's':
            if update_product(int(product['id']), int(new_code), new_name, float(new_price), int(new_stock)):
                print('Producto actualizado correctamente.')
                time.sleep(3)
                break
        elif prompt_confirm == 'n':
            clear_screen()
            display_back_menu()
            break                            
        else:
            display_invalid_option()            

def update_product_dynamic(condition):
    display_title_menu(f'Actualizar por {condition}', 'V', 'letra')
    display_back_menu()
    condition = condition.upper()
    back = False
    while not back:
        prompt = input(f'\t Ingrese el {condition} del producto a ACTUALIZAR: ').strip()           
        if not validate_back(prompt) and (back := True):
            clear_screen()
            break
        else:                        
            if condition == 'ID':
                if validate_id(prompt):
                    product_id = int(prompt)
                    product = search_product('id', product_id)
                    if product:
                        new_data_product(product)          
                    else:
                        display_not_found(f'producto con ID: {product_id}')                        
                else:
                    display_invalid_id()
            elif condition == 'CÓDIGO':
                if validate_code(prompt):
                    code = int(prompt)
                    product = search_product('code', code)
                    if product:
                        new_data_product(product)          
                    else:
                        display_not_found(f'producto con CODIGO: {code}')
                else:
                    display_invalid_code()                        
            else:
                if validate_name(prompt): 
                    name = prompt.capitalize()                   
                    product = search_product('name', name)
                    if product:
                        new_data_product(product)          
                    else:
                        display_not_found(f'producto con NOMBRE: {name}') 
                else:
                    display_invalid_name()                                                            

def update_product_controller(condition):
    condition = condition.upper()
    if condition == 'ID':
        update_product_dynamic(condition)
    elif condition == 'CÓDIGO':
        update_product_dynamic(condition)
    else:
        update_product_dynamic(condition)

def low_stock_report_controller():
    products = get_low_stock_products()
    if products:        
        display_products(products, 'REPORTE de PRODUCTOS con stock bajo')
    else:
        display_not_found('productos con stock bajo')
        time.sleep(3)
