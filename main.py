from utils.db_utils import connect_to_db, create_tables
from services.product_service import add_product, list_products, list_product, modify_product, remove_product

def main():
    menu()

def menu():
    conn = connect_to_db()
    create_tables(conn)    
    while True:
        print("\nMenú E-commerce")
        print("1. Agregar producto")
        print("2. Listar productos")
        print("3. Mostrar producto por ID")
        print("4. Actualizar producto")
        print("5. Eliminar producto por ID")
        print("6. Salir")
        option = input("Selecciona una opción: ")

        if option == "1":
            add_product(conn)
        elif option == "2":
            list_products(conn)
        elif option == "3":
            list_product(conn)
        elif option == "4":
            modify_product(conn)
        elif option == "5":
            remove_product(conn)
        elif option == "6":
            break
        else:
            print("Opción no válida")
    conn.close()

if __name__ == "__main__":
    main()