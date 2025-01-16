import streamlit as st
from ..inventory.product import Product
from ..inventory.inventory_manager import InventoryManager
from ..inventory.user_manager import UserManager
from ..inventory.user import UserRole
from ..inventory.cart import Cart
from .payments import PaymentProcessor, PaymentDetails
from .styles import apply_custom_styles
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize session state
if 'cart' not in st.session_state:
    st.session_state.cart = Cart()
if 'checkout_step' not in st.session_state:
    st.session_state.checkout_step = 1
if 'payment_processor' not in st.session_state:
    st.session_state.payment_processor = PaymentProcessor()

def init_app():
    """Initialize the application state"""
    if 'inventory_manager' not in st.session_state:
        st.session_state.inventory_manager = InventoryManager()

        # Add Starlink products
        st.session_state.inventory_manager.add_product(
            "Starlink Standard Kit",
            599.00,
            50
        )
        st.session_state.inventory_manager.add_product(
            "Starlink High Performance Kit",
            2500.00,
            25
        )
        st.session_state.inventory_manager.add_product(
            "Starlink Maritime",
            5000.00,
            10
        )
        st.session_state.inventory_manager.add_product(
            "Starlink RV Kit",
            599.00,
            30
        )
        st.session_state.inventory_manager.add_product(
            "Starlink Mobility Kit",
            2500.00,
            15
        )
        st.session_state.inventory_manager.add_product(
            "Starlink Aviation Terminal",
            150000.00,
            5
        )

    if 'user_manager' not in st.session_state:
        st.session_state.user_manager = UserManager()