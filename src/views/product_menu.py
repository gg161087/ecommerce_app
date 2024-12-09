from src.utils.displayer import (
    display_menu, 
    display_dynamic_selector, 
    clear_screen, 
    display_closing_program, 
    display_invalid_option,
    display_report_menu
)
from src.controllers.product_controller import (
    create_product_controller,
    list_products_controller,
    search_product_controller,
    update_product_controller,
    remove_product_controller,
    low_stock_report_controller,
    list_products_removed
)

def product_menu():
    clear_screen()
    while True:        
        display_menu()
        prompt = input('\t Seleccione una opción: ').strip()
        if prompt.isnumeric():
            option = int(prompt)
            if option > 0 and option <= 7:
                match option:
                    case 1:
                        clear_screen()
                        create_product_controller()
                    case 2:
                        clear_screen()
                        list_products_controller() 
                    case 3:  
                        clear_screen()                        
                        search_product_menu()
                    case 4:
                        clear_screen()
                        update_product_menu()
                    case 5:
                        clear_screen()
                        report_product_menu()
                    case 6:
                        clear_screen()
                        remove_product_menu()
                    case 7:
                        display_closing_program()
                        break
            else:
                clear_screen()
                display_invalid_option()  
        else:
            clear_screen()
            display_invalid_option()

def search_product_menu():
    while True:
        clear_screen()
        display_dynamic_selector('Buscar')
        prompt = input('\t Seleccione una opción: ')
        if prompt.isnumeric():
            option = int(prompt)
            if option > 0 and option <= 4:
                match option:
                    case 1:
                        clear_screen()
                        search_product_controller('id')                     
                    case 2:
                        clear_screen()
                        search_product_controller('code') 
                    case 3:  
                        clear_screen()
                        search_product_controller('name')
                    case 4:
                        clear_screen()                        
                        break
            else:
                clear_screen()
                display_invalid_option()  
        else:
            clear_screen()
            display_invalid_option()

def remove_product_menu():    
    while True:
        clear_screen()
        display_dynamic_selector('Eliminar')
        prompt = input('\t Seleccione una opción: ')
        if prompt.isnumeric():
            option = int(prompt)
            if option > 0 and option <= 4:
                match option:
                    case 1:
                        clear_screen()
                        remove_product_controller('id')                        
                    case 2:
                        clear_screen()
                        remove_product_controller('code')
                    case 3:  
                        clear_screen()
                        remove_product_controller('name')
                    case 4:
                        clear_screen()                        
                        break
            else:
                clear_screen()
                display_invalid_option()  
        else:
            clear_screen()
            display_invalid_option()

def update_product_menu():
    while True:
        clear_screen()
        display_dynamic_selector('Buscar y Actualizar')
        prompt = input('\t Seleccione una opción: ')
        if prompt.isnumeric():
            option = int(prompt)
            if option > 0 and option <= 4:
                match option:
                    case 1:
                        clear_screen()
                        update_product_controller('id')                        
                    case 2:
                        clear_screen()
                        update_product_controller('code')
                    case 3:  
                        clear_screen()
                        update_product_controller('name')
                    case 4:
                        clear_screen()                        
                        break
            else:
                clear_screen()
                display_invalid_option()  
        else:
            clear_screen()
            display_invalid_option()

def report_product_menu():
    while True:
        clear_screen()
        display_report_menu()
        prompt = input('\t Seleccione una opción: ')
        if prompt.isnumeric():
            option = int(prompt)
            if option > 0 and option <= 3:
                match option:
                    case 1:
                        clear_screen()
                        low_stock_report_controller()                       
                    case 2:
                        clear_screen()
                        list_products_removed()
                    case 3:  
                        clear_screen()
                        break                    
            else:
                clear_screen()
                display_invalid_option()  
        else:
            clear_screen()
            display_invalid_option()
