from inventory.product import Product
from inventory.inventory_manager import InventoryManager

class Cart:
    def __init__(self):
        self.cart_items = {}

    def add_to_cart(self, product: Product, quantity: int):
        if product.name in self.cart_items:
            self.cart_items[product.name]['quantity'] += quantity
        else:
            self.cart_items[product.name] = {
                'product': product,
                'quantity': quantity
            }

    def remove_from_cart(self, product_name: str):
        try:
            if product_name in self.cart_items:
                del self.cart_items[product_name]
                print(f"Product '{product_name}' removed from cart.")
            else:
                raise KeyError ("Product not found in cart.")
        except KeyError as e:
            print(f"Error: {e}")
        
        
        # if product_name in self.cart_items:
        #     del self.cart_items[product_name]

    def view_cart(self):
        # Return a list of item descriptions for readability
        return [
            f"{item['product'].get_product_info()}, In Cart: {item['quantity']}"
            for item in self.cart_items.values()
        ]

    def calculate_cart_total(self):
        return sum(
            item['product'].price * item['quantity']
            for item in self.cart_items.values()
        )
