import os
from colorama import Fore, Back, init
init(autoreset=True)

def display_divider():
    print(Fore.YELLOW + '-' * 70)

def display_table_headers():
    print(f'\t{Back.GREEN}{"#":<5}{"Producto":<15}{"Precio($)":>15}{"Stock":>15}')

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_product(product):    
    print(f'\t{product['id']:<5}{product['name']:<15}{product['price']:>15.2f}{product['stock']:>15}')

def display_products(products):
    display_divider()
    display_table_headers()
    for product in products:
        display_product(product)

def display_back_menu():
    display_divider()
    print(f'Para volver al menú anterior escriba la letra "{Fore.YELLOW}v{Fore.RESET}"')
    display_divider()

def display_product_requirements():
    display_divider()
    print(f'El nombre debe tener al menos 3 caracteres, stock numérico y el \nprecio numérico/mayor que 0.')
    display_divider()

def display_menu():
    display_divider()
    print(f'Menú {Back.YELLOW}{Fore.BLACK}E-commerce{Back.RESET}{Fore.RESET}, Escriba número de opcion ({Fore.YELLOW}1-7{Fore.RESET}):'.center(50))
    print(f'\t {Fore.YELLOW}1{Fore.RESET}. {Fore.GREEN}Agregar Producto')
    print(f'\t {Fore.YELLOW}2{Fore.RESET}. {Fore.WHITE}Listar Productos')
    print(f'\t {Fore.YELLOW}3{Fore.RESET}. {Fore.BLUE}Buscar Producto')
    print(f'\t {Fore.YELLOW}4{Fore.RESET}. {Fore.MAGENTA}Editar Producto')
    print(f'\t {Fore.YELLOW}5{Fore.RESET}. {Fore.CYAN}Reporte Productos bajo de Stock')
    print(f'\t {Fore.YELLOW}6{Fore.RESET}. {Fore.RED}Eliminar Producto')
    print(f'\t {Fore.YELLOW}7{Fore.RESET}. Salir')
    display_divider()

def display_closing_program():
    print(f'GRACIAS por usar {Back.YELLOW}{Fore.BLACK}E-commerce{Back.RESET}{Fore.RESET}. Saliendo del programa...')

def display_invalid_option():
    print('\t Opción no válida, intente de nuevo: ')
