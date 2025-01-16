from inventory.product import Product
from inventory.inventory_manager import InventoryManager
from inventory.cart import Cart

def main():
    # Create an InventoryManager instance
    inventory_manager = InventoryManager()

    # Create some products
    product1 = Product("Laptop", 1000.00, 5)
    product2 = Product("Smartphone", 500.00, 10)

    # Add products to inventory
    inventory_manager.add_product(product1)
    inventory_manager.add_product(product2)

    # Display product details
    print("Initial Inventory:")
    for product in inventory_manager.products:
        print(product.get_product_info())

    # Create a cart
    cart = Cart()

    # Add items to the cart
    cart.add_to_cart(product1, 2)
    cart.add_to_cart(product2, 3)

    # View cart details
    print("\nCart Details:")
    for item in cart.view_cart():
        print(item)

    # Calculate and display total inventory value
    print(f"\nTotal Inventory Value: {inventory_manager.get_total_inventory_value():.2f} €")

    # Calculate and display cart total
    print(f"Total Cart Value: {cart.calculate_cart_total():.2f} €")

if __name__ == "__main__":
    main()
