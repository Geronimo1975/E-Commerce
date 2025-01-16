import unittest
from inventory_management_system.inventory.inventory_manager import InventoryManager
from inventory_management_system.inventory.product import Product

class TestInventoryManager(unittest.TestCase):
    def setUp(self):
        self.inventory_manager = InventoryManager()
        
    def test_add_product(self):
        product = self.inventory_manager.add_product("Test Product", 10.99, 5)
        self.assertIsInstance(product, Product)
        self.assertEqual(product.name, "Test Product")
        self.assertEqual(product.price, 10.99)
        self.assertEqual(product.quantity, 5)
        
    def test_add_duplicate_product(self):
        self.inventory_manager.add_product("Test Product", 10.99, 5)
        with self.assertRaises(ValueError):
            self.inventory_manager.add_product("Test Product", 15.99, 3)
            
    def test_remove_product(self):
        self.inventory_manager.add_product("Test Product", 10.99, 5)
        self.inventory_manager.remove_product("Test Product")
        self.assertEqual(len(self.inventory_manager.products), 0)
        
    def test_update_product_quantity(self):
        self.inventory_manager.add_product("Test Product", 10.99, 5)
        self.inventory_manager.update_product_quantity("Test Product", 10)
        product_info = self.inventory_manager.get_product_info("Test Product")
        self.assertIn("10", product_info)
        
    def test_get_total_inventory_value(self):
        self.inventory_manager.add_product("Product 1", 10.00, 5)
        self.inventory_manager.add_product("Product 2", 20.00, 3)
        total_value = self.inventory_manager.get_total_inventory_value()
        self.assertEqual(total_value, 110.00)  # (10*5 + 20*3)

if __name__ == '__main__':
    unittest.main()
