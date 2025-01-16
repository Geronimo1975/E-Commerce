import unittest
from inventory_management_system.streamlit.payments import PaymentProcessor, PaymentDetails

class TestPayments(unittest.TestCase):
    def setUp(self):
        self.payment_processor = PaymentProcessor()
        self.valid_payment = PaymentDetails(
            card_number="4111111111111111",
            expiry_month=12,
            expiry_year=25,
            cvv="123",
            amount=100.00
        )
        
    def test_valid_payment(self):
        result = self.payment_processor.process_payment(self.valid_payment)
        self.assertTrue(result.success)
        self.assertIsNotNone(result.transaction_id)
        self.assertIsNone(result.error_message)
        
    def test_invalid_card_number(self):
        invalid_payment = PaymentDetails(
            card_number="1234",
            expiry_month=12,
            expiry_year=25,
            cvv="123",
            amount=100.00
        )
        result = self.payment_processor.process_payment(invalid_payment)
        self.assertFalse(result.success)
        self.assertIsNone(result.transaction_id)
        self.assertEqual(result.error_message, "Invalid card details")
        
    def test_expired_card(self):
        expired_payment = PaymentDetails(
            card_number="4111111111111111",
            expiry_month=1,
            expiry_year=20,
            cvv="123",
            amount=100.00
        )
        result = self.payment_processor.process_payment(expired_payment)
        self.assertFalse(result.success)
        self.assertIsNone(result.transaction_id)
        self.assertEqual(result.error_message, "Invalid card details")

if __name__ == '__main__':
    unittest.main()
