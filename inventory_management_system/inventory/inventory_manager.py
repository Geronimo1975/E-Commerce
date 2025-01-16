from .product import Product
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class InventoryManager:
    def __init__(self):
        self.products = []

    def add_product(self, name, price, quantity):
        product = Product(name, price, quantity)
        try:
            for item in self.products:
                if item.name == name:
                    raise ValueError("Product already exists.")
            self.products.append(product)
            logger.info(f"Added product: {name}")
            return product
        except ValueError as e:
            logger.error(f"Error adding product: {e}")
            raise

    def remove_product(self, product_name: str):
        try:
            self.products = [
                p for p in self.products if p.name != product_name
            ]
            logger.info(f"Removed product: {product_name}")
        except Exception as e:
            logger.error(f"Error removing product: {e}")
            raise

    def update_product_quantity(self, product_name: str, new_quantity: int):
        try:
            for product in self.products:
                if product.name == product_name:
                    product.update_quantity(new_quantity)
                    logger.info(f"Updated {product_name} quantity to {new_quantity}")
                    return
            raise ValueError("Product not found")
        except Exception as e:
            logger.error(f"Error updating quantity: {e}")
            raise

    def get_product_info(self, product_name: str):
        for product in self.products:
            if product.name == product_name:
                return product.get_product_info()
        return "Product not found."

    def get_all_products(self):
        return [
            {
                'name': p.name,
                'price': p.price,
                'quantity': p.quantity,
                'total_value': p.price * p.quantity
            }
            for p in self.products
        ]

    def get_total_inventory_value(self):
        return sum(p.price * p.quantity for p in self.products)
