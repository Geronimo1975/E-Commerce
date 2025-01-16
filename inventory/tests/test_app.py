
import unittest
from inventory.streamlit.ecommerce_app import init_app

class TestApp(unittest.TestCase):
    def test_init_app(self):
        # Basic test to ensure the app initializes
        try:
            init_app()
            self.assertTrue(True)
        except Exception as e:
            self.fail(f"App initialization failed: {e}")

if __name__ == '__main__':
    unittest.main()
