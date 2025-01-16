from inventory.product import Product
from typing import Dict, Optional, List
import logging
#from .database import get_db_cursor


# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
class InventoryManager:
    def __init__(self):
        self.products = []

    def add_product(self, product: Product):
        try:
            for item in self.products:
                if item == product:
                    raise ValueError("Product already exists.")
            self.products.append(product)
        except ValueError as e:
            print(f"Error adding product:\n{e}\n")

    def remove_product(self, product_name: str):
        try:
            self.products = [
                p for p in self.products if p.name != product_name
            ]
        except Exception as e:
            print(f"Error removing product:\n{e}\n")

    def remove_product(self, product_name: str):
        self.products = [
            p for p in self.products
            if p.name != product_name
        ]

    def update_product_quantity(self, product_name: str, new_quantity: int):
        try:
            for product in self.products:
                if product.name == product_name:
                    product.update_quantity(new_quantity)
                    print(
                        f"Updated {product_name} quantity to {new_quantity}."
                    )
                else:
                    raise ValueError("Product not found.")
        except ValueError as e:
            print(f"Error:\n{e}\n")

    def get_product_info(self, product_name: str):
        for product in self.products:
            if product.name == product_name:
                return product.get_product_info()
        return "Product not found."
    
    

    def get_total_inventory_value(self):
        return sum(p.price * p.quantity for p in self.products)
