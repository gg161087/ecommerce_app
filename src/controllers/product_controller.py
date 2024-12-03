from src.utils.messages import display_menu, clear_screen, display_closing_program, display_invalid_option
from src.services.product_service import add_product, list_products, retrieve_product, edit_product, delete_product_by_id, low_stock_report

def product_menu():
    clear_screen()
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
                        retrieve_product()
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
