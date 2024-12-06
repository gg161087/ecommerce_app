import os
from colorama import Fore, Back, init
init(autoreset=True)

def display_divider():
    print(Fore.YELLOW + '-' * 78)

def display_table_headers():
    print(f'\t{Back.GREEN}{"#":<5}{"Código":<12}{"Producto":<15}{"Precio($)":>15}{"Stock":>15}')

def display_paginated_controls():
    print(f'Opciones: [{Fore.YELLOW}S{Fore.RESET}] Siguiente | [{Fore.YELLOW}A{Fore.RESET}] Anterior | [{Fore.YELLOW}V{Fore.RESET}] Volver')

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_product(product):    
    print(f'\t{product['id']:<5}{product['code']:<12}{product['name']:<15}{product['price']:>15.2f}{product['stock']:>15}')

def paginate_list(items, page_size=5):
    # Divide una lista en páginas de tamaño fijo.    
    for i in range(0, len(items), page_size):
        yield items[i:i + page_size]

def display_products(products, page_size=5):
    # Muestra los productos en forma paginada en la consola.  
    paginated = list(paginate_list(products, page_size))
    total_pages = len(paginated)
    current_page = 0
    while True:
        display_back_menu()
        display_table_headers()
        for product in paginated[current_page]:
            display_product(product)
        if total_pages > 1:
            display_divider()
            print(f'Página {current_page + 1} de {total_pages}')     
            display_paginated_controls()
        display_divider()
        choice = input('\tSeleccione una opción: ').strip().lower()
        if choice == 's':
            if current_page < total_pages - 1:
                current_page += 1
            else:
                print('Ya estás en la última página.')
        elif choice == 'a':
            if current_page > 0:
                current_page -= 1
            else:
                print('Ya estás en la primera página.')
        elif choice == 'v':
            break
        else:
            print('Opción no válida. Por favor, intente de nuevo.')

def display_back_menu():
    display_divider()
    print(f'Para volver al menú anterior escriba la letra [{Fore.YELLOW}V{Fore.RESET}]')
    display_divider()

def display_product_requirements():
    display_divider()
    print(f'El nombre debe tener al menos 3 caracteres, stock numérico y el \nprecio numérico/mayor que 0.')
    display_divider()

def display_menu():
    display_divider()
    print(f'Menú {Back.YELLOW}{Fore.BLACK}E-commerce{Back.RESET}{Fore.RESET}, Escriba número de opcion ({Fore.YELLOW}1-7{Fore.RESET}):'.center(50))
    display_divider()
    print(f'\t [{Fore.YELLOW}1{Fore.RESET}] {Fore.GREEN}Agregar Producto')
    print(f'\t [{Fore.YELLOW}2{Fore.RESET}] {Fore.WHITE}Listar Productos')
    print(f'\t [{Fore.YELLOW}3{Fore.RESET}] {Fore.BLUE}Buscar Producto')
    print(f'\t [{Fore.YELLOW}4{Fore.RESET}] {Fore.MAGENTA}Editar Producto')
    print(f'\t [{Fore.YELLOW}5{Fore.RESET}] {Fore.CYAN}Reporte Productos bajo de Stock')
    print(f'\t [{Fore.YELLOW}6{Fore.RESET}] {Fore.RED}Eliminar Producto')
    print(f'\t [{Fore.YELLOW}7{Fore.RESET}] Salir')
    display_divider()

def display_closing_program():
    print(f'GRACIAS por usar {Back.YELLOW}{Fore.BLACK}E-commerce{Back.RESET}{Fore.RESET}. Saliendo del programa...')

def display_invalid_option():
    print('\t Opción no válida, intente de nuevo: ')

def display_dynamic_selector(selector):
    display_divider()
    print(f'Menú {selector} Producto, Escriba número de opcion ({Fore.YELLOW}1-4{Fore.RESET}):'.center(50))
    display_divider()
    print(f'\t [{Fore.YELLOW}1{Fore.RESET}] {Fore.GREEN}{selector} Producto por ID')
    print(f'\t [{Fore.YELLOW}2{Fore.RESET}] {Fore.WHITE}{selector} Producto por CÓDIGO')
    print(f'\t [{Fore.YELLOW}3{Fore.RESET}] {Fore.BLUE}{selector} Producto por NOMBRE')
    print(f'\t [{Fore.YELLOW}4{Fore.RESET}] Volver')
    display_divider()