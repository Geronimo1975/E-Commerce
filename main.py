
from inventory.core.inventory_manager import InventoryManager
from inventory.core.product import Product
from inventory.core.cart import Cart

def main():
    # Create an InventoryManager instance
    inventory_manager = InventoryManager()

    # Create some products
    product1 = Product("Laptop", 1000.00, 5)
    product2 = Product("Smartphone", 500.00, 10)

    # Add products to inventory
    inventory_manager.add_product(product1)
    inventory_manager.add_product(product2)

    # Create a cart
    cart = Cart()
    
    # Add items to cart
    cart.add_to_cart(product1, 2)
    cart.add_to_cart(product2, 3)

    # Display results
    print("\nInventory Status:")
    for product in inventory_manager.products:
        print(product.get_product_info())

    print("\nCart Status:")
    for item in cart.view_cart():
        print(item)

if __name__ == "__main__":
    main()
