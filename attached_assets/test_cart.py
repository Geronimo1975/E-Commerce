import unittest
from inventory.product import Product
from inventory.cart import Cart

class TestCart(unittest.TestCase):
    def setUp(self):
        self.cart = Cart()
        self.product1 = Product("Laptop", 1000.00, 5)
        self.product2 = Product("Smartphone", 500.00, 10)

    def test_add_to_cart(self):
        self.cart.add_to_cart(self.product1, 2)
        self.assertIn("Laptop", self.cart.cart_items)
        self.assertEqual(self.cart.cart_items["Laptop"]["quantity"], 2)

        # Add same product again; quantity should increase
        self.cart.add_to_cart(self.product1, 3)
        self.assertEqual(self.cart.cart_items["Laptop"]["quantity"], 5)

    def test_remove_from_cart(self):
        # Add then remove
        self.cart.add_to_cart(self.product2, 4)
        self.assertIn("Smartphone", self.cart.cart_items)
        
        self.cart.remove_from_cart("Smartphone")
        self.assertNotIn("Smartphone", self.cart.cart_items)

    def test_view_cart(self):
        self.cart.add_to_cart(self.product1, 1)
        cart_view = self.cart.view_cart()
        self.assertTrue(len(cart_view) > 0)
        self.assertIn("Laptop", cart_view[0])

    def test_calculate_cart_total(self):
        self.cart.add_to_cart(self.product1, 2)  # 2 * 1000.00 = 2000
        self.cart.add_to_cart(self.product2, 3)  # 3 * 500.00  = 1500
        self.assertEqual(self.cart.calculate_cart_total(), 3500.00)

if __name__ == '__main__':
    unittest.main()
