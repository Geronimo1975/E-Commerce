import streamlit as st
from inventory_management_system.inventory.product import Product
from inventory_management_system.inventory.inventory_manager import InventoryManager
from inventory_management_system.inventory.user_manager import UserManager
from inventory_management_system.inventory.user import UserRole
from inventory_management_system.inventory.cart import Cart
from inventory_management_system.streamlit.payments import PaymentProcessor, PaymentDetails
from inventory_management_system.streamlit.styles import apply_custom_styles
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

# Initialize the application
init_app()

# Apply custom styles
apply_custom_styles()

# Create main page layout
st.title("Starlink E-commerce Platform")

# Display products
st.header("Available Products")
for product in st.session_state.inventory_manager.products:
    with st.container():
        col1, col2, col3 = st.columns([2, 1, 1])
        with col1:
            st.write(f"### {product.name}")
            st.write(f"Price: ${product.price:.2f}")
            st.write(f"Available: {product.quantity}")
        with col2:
            quantity = st.number_input(f"Quantity for {product.name}", 
                                    min_value=0, 
                                    max_value=product.quantity, 
                                    value=0,
                                    key=f"qty_{product.name}")
        with col3:
            if st.button("Add to Cart", key=f"add_{product.name}") and quantity > 0:
                st.session_state.cart.add_to_cart(product, quantity)
                st.success(f"Added {quantity} {product.name} to cart!")

# Display cart
st.sidebar.header("Shopping Cart")
cart_items = st.session_state.cart.cart_items
if not cart_items:
    st.sidebar.write("Cart is empty")
else:
    for item_name, item_data in cart_items.items():
        st.sidebar.write(f"{item_name} (x{item_data['quantity']})")
        if st.sidebar.button("Remove", key=f"remove_{item_name}"):
            st.session_state.cart.remove_from_cart(item_name)
            st.rerun()

    total = st.session_state.cart.calculate_cart_total()
    st.sidebar.write(f"Total: ${total:.2f}")

    if st.sidebar.button("Proceed to Checkout"):
        st.session_state.checkout_step = 2