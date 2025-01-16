import unittest
from datetime import datetime
from payments import PaymentProcessor, PaymentDetails

class TestPaymentProcessor(unittest.TestCase):
    def setUp(self):
        self.payment_processor = PaymentProcessor()
        self.valid_payment = PaymentDetails(
            card_number="4532 0123 4567 8901",
            expiry_month=12,
            expiry_year=25,
            cvv="123",
            amount=99.99
        )

    def test_valid_payment(self):
        result = self.payment_processor.process_payment(self.valid_payment)
        self.assertTrue(result.success)
        self.assertIsNotNone(result.transaction_id)
        self.assertIsNone(result.error_message)
        
    def test_expired_card(self):
        payment = PaymentDetails(
            card_number="4532 0123 4567 8901",
            expiry_month=1,
            expiry_year=20,
            cvv="123",
            amount=99.99
        )
        result = self.payment_processor.process_payment(payment)
        self.assertFalse(result.success)
        self.assertIsNone(result.transaction_id)
        self.assertEqual(result.error_message, "Invalid card details")
        
    def test_invalid_card_number(self):
        payment = PaymentDetails(
            card_number="1234",
            expiry_month=12,
            expiry_year=25,
            cvv="123",
            amount=99.99
        )
        result = self.payment_processor.process_payment(payment)
        self.assertFalse(result.success)
        
    def test_invalid_cvv(self):
        payment = PaymentDetails(
            card_number="4532 0123 4567 8901",
            expiry_month=12,
            expiry_year=25,
            cvv="12",
            amount=99.99
        )
        result = self.payment_processor.process_payment(payment)
        self.assertFalse(result.success)

if __name__ == '__main__':
    unittest.main()
