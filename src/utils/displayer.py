import os
from colorama import Fore, Back, init
init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_divider():
    print(Fore.YELLOW + '-' * 78)

def display_table_headers():
    print(f'\t{Back.GREEN}{"#":<5}{"Código":<12}{"Producto":<15}{"Precio($)":>15}{"Stock":>15}')

def display_confirm(dynamic):
    display_divider()
    print(f'Desea {dynamic}: [{Fore.YELLOW}S{Fore.RESET}] Si | [{Fore.YELLOW}N{Fore.RESET}] No')
    display_divider()

def display_title_menu(name, range, nan='número'):
    display_divider()
    print(f'Menú {name}, Escriba {nan} de opcion ({Fore.YELLOW}{range}{Fore.RESET}):'.center(50))
    display_divider()

def display_paginated_controls(cpage, tpage):
    display_divider()
    print(f'Página {cpage + 1} de {tpage}.  Opciones: [{Fore.YELLOW}S{Fore.RESET}] Siguiente | [{Fore.YELLOW}A{Fore.RESET}] Anterior | [{Fore.YELLOW}V{Fore.RESET}] Volver')
    display_divider()

def display_product(product):    
    print(f'\t{product['id']:<5}{product['code']:<12}{product['name']:<15}{product['price']:>15.2f}{product['stock']:>15}')

def paginate_list(items, page_size=5):
    # Divide una lista en páginas de tamaño fijo.    
    for i in range(0, len(items), page_size):
        yield items[i:i + page_size]

def display_invalid_data():
    display_divider()
    print('Datos ingresados incorrectos, intente de nuevo.')
    display_divider()

def display_invalid_id():
    display_divider()
    print('El ID del producto debe ser numerico y mayor que 0.')
    display_divider()

def display_invalid_code():
    display_divider() 
    print('El CÓDIGO debe ser numérico y de 4 cifras.')
    display_divider() 

def display_invalid_name():
    display_divider()
    print('El NOMBRE del producto debe tener al menos 3 caracteres.')
    display_divider()

def display_products(products, title, page_size=5):
    # Muestra los productos en forma paginada en la consola. 
    back = False 
    paginated = list(paginate_list(products, page_size))
    total_pages = len(paginated)
    options = ''
    if total_pages > 1:
        options = 'S-A-V'
    else:
        options = 'V'
    current_page = 0
    def table_products(): 
        clear_screen()        
        display_title_menu(title, options, 'letra')
        display_back_menu()
        display_table_headers()       
        for product in paginated[current_page]:
            display_product(product)
        display_divider()
        print(f'\tProductos Total: {len(products)}') 
        if total_pages > 1:
            display_paginated_controls(current_page, total_pages)
        else:
            display_divider()
    table_products()
    while not back:
        choice = input('\tSeleccione una opción: ').strip().lower()            
        if choice.lower() == 's':                        
            if current_page < total_pages - 1:                
                current_page += 1
                table_products()
            else:
                table_products()                                               
                print('\tYa estás en la última página.')
                display_divider()
        elif choice.lower() == 'a':                        
            if current_page > 0:                
                current_page -= 1
                table_products()
            else: 
                table_products()                             
                print('\tYa estás en la primera página.')
                display_divider()
        elif choice.lower() == 'v':
            back = True
            clear_screen()           
            break
        else:            
            table_products()            
            display_invalid_option(top_divider=False)          

def display_back_menu():    
    print(f'Para volver al menú anterior escriba la letra [{Fore.YELLOW}V{Fore.RESET}]')
    display_divider()

def display_product_requirements():    
    print(f'El código debe ser numérico y de 4 cifras, \nEl nombre debe tener al menos 3 caracteres, \nEl stock numérico mayor o igual a 0 y \nEl precio numérico/mayor que 0.')
    display_divider()

def display_menu():
    display_title_menu(f'{Back.YELLOW}{Fore.BLACK}E-commerce{Back.RESET}{Fore.RESET}', '1-7')
    print(f'\t [{Fore.YELLOW}1{Fore.RESET}] {Fore.GREEN}Agregar Producto')
    print(f'\t [{Fore.YELLOW}2{Fore.RESET}] {Fore.WHITE}Listar Productos')
    print(f'\t [{Fore.YELLOW}3{Fore.RESET}] {Fore.BLUE}Buscar Producto')
    print(f'\t [{Fore.YELLOW}4{Fore.RESET}] {Fore.MAGENTA}Actualizar Producto')
    print(f'\t [{Fore.YELLOW}5{Fore.RESET}] {Fore.CYAN}Reportes de Productos')
    print(f'\t [{Fore.YELLOW}6{Fore.RESET}] {Fore.RED}Eliminar Producto')
    print(f'\t [{Fore.YELLOW}7{Fore.RESET}] Salir')
    display_divider()

def display_closing_program():
    print(f'GRACIAS por usar {Back.YELLOW}{Fore.BLACK}E-commerce{Back.RESET}{Fore.RESET}. Saliendo del programa...')

def display_invalid_option(top_divider=True):
    if top_divider:   
        display_divider()
    print('\tOpción no válida, intente de nuevo.')
    display_divider()

def display_dynamic_selector(selector):
    display_title_menu(f'{selector} Producto', '1-4')
    print(f'\t [{Fore.YELLOW}1{Fore.RESET}] {Fore.GREEN}{selector} Producto por ID')
    print(f'\t [{Fore.YELLOW}2{Fore.RESET}] {Fore.WHITE}{selector} Producto por CÓDIGO')
    print(f'\t [{Fore.YELLOW}3{Fore.RESET}] {Fore.BLUE}{selector} Producto por NOMBRE')
    print(f'\t [{Fore.YELLOW}4{Fore.RESET}] Volver')
    display_divider()

def display_report_menu():
    display_title_menu('REPORTES de Productos', '1-3')
    print(f'\t [{Fore.YELLOW}1{Fore.RESET}] {Fore.YELLOW}Productos Bajo de Stock')
    print(f'\t [{Fore.YELLOW}2{Fore.RESET}] {Fore.RED}Productos ELIMINADOS')
    print(f'\t [{Fore.YELLOW}3{Fore.RESET}] Volver')
    display_divider()

def display_not_found(message):
    clear_screen()
    display_back_menu()
    print(f'No se encontró/encontraron {Fore.YELLOW}{message}{Fore.RESET}.'.center(50))
    display_divider()

def display_remove_message():
    clear_screen()
    display_back_menu()
    display_divider()
    print('Producto eliminado correctamente.')
    display_divider()