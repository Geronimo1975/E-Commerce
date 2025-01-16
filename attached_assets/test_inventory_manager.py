import unittest
from inventory.product import Product
from inventory.inventory_manager import InventoryManager

class TestInventoryManager(unittest.TestCase):
    def setUp(self):
        self.inventory_manager = InventoryManager()
        self.product1 = Product("Laptop", 1000.00, 5)
        self.product2 = Product("Smartphone", 500.00, 10)

        # Add two products to the inventory
        self.inventory_manager.add_product(self.product1)
        self.inventory_manager.add_product(self.product2)

    def test_add_product(self):
        self.assertEqual(len(self.inventory_manager.products), 2)
        new_product = Product("Tablet", 300.00, 3)
        self.inventory_manager.add_product(new_product)
        self.assertEqual(len(self.inventory_manager.products), 3)

    def test_remove_product(self):
        # Remove one product
        self.inventory_manager.remove_product("Laptop")
        product_names = [p.name for p in self.inventory_manager.products]
        self.assertNotIn("Laptop", product_names)
        self.assertIn("Smartphone", product_names)

    def test_update_product_quantity(self):
        # Update the "Laptop" quantity
        updated = self.inventory_manager.update_product_quantity("Laptop", 8)
        # self.assertTrue(updated)
        # Ensure the laptop quantity is updated
        self.assertEqual(self.product1.quantity, 8)

    def test_get_product_info(self):
        info = self.inventory_manager.get_product_info("Laptop")
        self.assertIn("Laptop", info)
        self.assertIn("1000.00", info)

    def test_get_total_inventory_value(self):
        total_value = self.inventory_manager.get_total_inventory_value()
        # 5 laptops at 1000.00, 10 smartphones at 500.00 => 5*1000 + 10*500 = 5000 + 5000 = 10000
        self.assertEqual(total_value, 10000)

if __name__ == '__main__':
    unittest.main()
