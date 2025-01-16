
import unittest
from inventory.core.inventory_manager import InventoryManager
from inventory.core.product import Product

class TestInventoryManager(unittest.TestCase):
    def setUp(self):
        self.inventory = InventoryManager()

    def test_add_product(self):
        product = self.inventory.add_product("Test Product", 10.0, 5)
        self.assertEqual(len(self.inventory.products), 1)
        self.assertEqual(product.name, "Test Product")

if __name__ == '__main__':
    unittest.main()
