import unittest
from inventory_management_system.inventory.inventory_manager import InventoryManager
from inventory_management_system.inventory.cart import Cart
from inventory_management_system.inventory.user_manager import UserManager
from inventory_management_system.inventory.user import UserRole

class TestApp(unittest.TestCase):
    def setUp(self):
        self.inventory_manager = InventoryManager()
        self.cart = Cart()
        self.user_manager = UserManager()
        
    def test_add_product_to_cart(self):
        # Add a product to inventory
        product = self.inventory_manager.add_product("Test Product", 10.99, 5)
        
        # Add product to cart
        self.cart.add_to_cart(product, 2)
        
        # Verify cart contents
        cart_items = self.cart.cart_items
        self.assertIn("Test Product", cart_items)
        self.assertEqual(cart_items["Test Product"]["quantity"], 2)
        
    def test_user_authentication(self):
        # Register a new user
        self.user_manager.register_user("testuser", "password123", UserRole.PARTNER)
        
        # Test authentication
        user = self.user_manager.authenticate_user("testuser", "password123")
        self.assertIsNotNone(user)
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.role, UserRole.PARTNER)
        
    def test_complete_purchase_flow(self):
        # Add product to inventory
        product = self.inventory_manager.add_product("Test Product", 10.99, 5)
        
        # Add to cart
        self.cart.add_to_cart(product, 2)
        
        # Calculate total
        total = self.cart.calculate_cart_total()
        self.assertEqual(total, 21.98)  # 10.99 * 2
        
        # Verify inventory quantity
        product_info = self.inventory_manager.get_product_info("Test Product")
        self.assertIn("5", product_info)  # Original quantity unchanged until purchase

if __name__ == '__main__':
    unittest.main()
