
import unittest
from inventory.core.cart import Cart
from inventory.core.product import Product

class TestCart(unittest.TestCase):
    def setUp(self):
        self.cart = Cart()
        self.product = Product("Test Product", 10.0, 5)

    def test_add_to_cart(self):
        self.cart.add_to_cart(self.product, 2)
        self.assertEqual(len(self.cart.cart_items), 1)

if __name__ == '__main__':
    unittest.main()
