import unittest
from inventory_management_system.inventory.cart import Cart
from inventory_management_system.inventory.product import Product

class TestCart(unittest.TestCase):
    def setUp(self):
        self.cart = Cart()
        self.product = Product("Test Product", 10.99, 5)
        
    def test_add_to_cart(self):
        self.cart.add_to_cart(self.product, 2)
        self.assertIn(self.product.name, self.cart.cart_items)
        self.assertEqual(self.cart.cart_items[self.product.name]['quantity'], 2)
        
    def test_add_existing_product(self):
        self.cart.add_to_cart(self.product, 2)
        self.cart.add_to_cart(self.product, 3)
        self.assertEqual(self.cart.cart_items[self.product.name]['quantity'], 5)
        
    def test_remove_from_cart(self):
        self.cart.add_to_cart(self.product, 2)
        self.cart.remove_from_cart(self.product.name)
        self.assertNotIn(self.product.name, self.cart.cart_items)
        
    def test_calculate_cart_total(self):
        product1 = Product("Product 1", 10.00, 5)
        product2 = Product("Product 2", 20.00, 3)
        self.cart.add_to_cart(product1, 2)
        self.cart.add_to_cart(product2, 1)
        total = self.cart.calculate_cart_total()
        self.assertEqual(total, 40.00)  # (10*2 + 20*1)

if __name__ == '__main__':
    unittest.main()
