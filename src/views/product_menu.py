from src.utils.displayer import display_menu, display_dynamic_selector, clear_screen, display_closing_program, display_invalid_option
from src.controllers.product_controller import (
    create_product_controller,
    list_products_controller,
    search_product_controller,
    update_product_controller,
    delete_product_controller,
    low_stock_report_controller,
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
                        update_product_controller()
                    case 5:
                        clear_screen()
                        low_stock_report_controller()
                    case 6:
                        clear_screen()
                        delete_product_controller()
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
    clear_screen()
    while True:
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
                        break
            else:
                clear_screen()
                display_invalid_option()  
        else:
            clear_screen()
            display_invalid_option()
 