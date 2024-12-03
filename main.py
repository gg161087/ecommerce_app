from src.controllers.product_controller import product_menu
from src.data.db_connection import initialize_db
        
if __name__ == "__main__":
    initialize_db()
    product_menu()
