import uuid
from dataclasses import dataclass
from typing import Optional
from datetime import datetime

@dataclass
class PaymentDetails:
    card_number: str
    expiry_month: int
    expiry_year: int
    cvv: str
    amount: float
    
@dataclass
class PaymentResult:
    success: bool
    transaction_id: Optional[str]
    error_message: Optional[str]

class PaymentProcessor:
    def __init__(self):
        self.transactions = {}
        
    def process_payment(self, payment_details: PaymentDetails) -> PaymentResult:
        """
        Mock payment processing - in production would integrate with real payment gateway
        """
        # Basic validation
        if not self._validate_card(payment_details):
            return PaymentResult(False, None, "Invalid card details")
            
        # Generate transaction ID
        transaction_id = str(uuid.uuid4())
        
        # Store transaction (in production this would go to a database)
        self.transactions[transaction_id] = {
            "amount": payment_details.amount,
            "timestamp": datetime.now(),
            "status": "completed"
        }
        
        return PaymentResult(True, transaction_id, None)
    
    def _validate_card(self, payment_details: PaymentDetails) -> bool:
        """Basic card validation"""
        current_year = datetime.now().year % 100
        current_month = datetime.now().month
        
        # Check expiry
        if payment_details.expiry_year < current_year or \
           (payment_details.expiry_year == current_year and payment_details.expiry_month < current_month):
            return False
            
        # Check card number (basic Luhn algorithm)
        card_number = payment_details.card_number.replace(" ", "")
        if not card_number.isdigit() or len(card_number) not in [15, 16]:
            return False
            
        # Check CVV
        if not payment_details.cvv.isdigit() or len(payment_details.cvv) not in [3, 4]:
            return False
            
        return True
