from src.models.product_model import (
    insert_product,
    fetch_all_products,
    fetch_product_dynamic,
    update_product_by_id,
    delete_product_by_id,
    fetch_low_stock_products,
)

def add_product(code, name, price, stock):
    insert_product(code, name, price, stock)

def get_all_products():
    return fetch_all_products()

def search_product(condition, parameter):
    return fetch_product_dynamic(condition, parameter)

def update_product(product_id, code, name, price, stock):
    return update_product_by_id(product_id, code, name, price, stock)

def delete_product(product_id):
    return delete_product_by_id(product_id)

def get_low_stock_products():
    return fetch_low_stock_products()
