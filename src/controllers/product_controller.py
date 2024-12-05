from src.utils.messages import display_menu, display_search_menu, clear_screen, display_closing_program, display_invalid_option
from src.services.product_service import add_product, list_products, retrieve_product_by_id, retrieve_product_by_name, retrieve_product_by_code, edit_product, delete_product_by_id, low_stock_report
from src.data.seed import seeder

def product_menu():
    clear_screen()
    seeder()
    while True:        
        display_menu()
        prompt = input('\t Seleccione una opción: ')
        if prompt.isnumeric():
            option = int(prompt)
            if option > 0 and option <= 7:
                match option:
                    case 1:
                        clear_screen()
                        add_product()
                    case 2:
                        clear_screen()
                        list_products() 
                    case 3:  
                        clear_screen()
                        #retrieve_product()
                        search_product_menu()
                    case 4:
                        clear_screen()
                        edit_product()
                    case 5:
                        clear_screen()
                        low_stock_report()
                    case 6:
                        clear_screen()
                        delete_product_by_id()
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
        display_search_menu('Buscar')
        prompt = input('\t Seleccione una opción: ')
        if prompt.isnumeric():
            option = int(prompt)
            if option > 0 and option <= 4:
                match option:
                    case 1:
                        clear_screen()
                        retrieve_product_by_id()
                    case 2:
                        clear_screen()
                        retrieve_product_by_code()
                    case 3:  
                        clear_screen()
                        retrieve_product_by_name()
                    case 4:                        
                        break
            else:
                clear_screen()
                display_invalid_option()  
        else:
            clear_screen()
            display_invalid_option()
 