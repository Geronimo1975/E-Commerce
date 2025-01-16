import streamlit as st
from inventory.product import Product
from inventory.inventory_manager import InventoryManager
from inventory.user_manager import UserManager
from inventory.user import UserRole
from inventory.cart import Cart
from payments import PaymentProcessor, PaymentDetails
from styles import apply_custom_styles
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

def display_product_grid():
    """Display products in a grid layout"""
    products = st.session_state.inventory_manager.products
    cols = st.columns(3)

    for idx, product in enumerate(products):
        with cols[idx % 3]:
            with st.container():
                st.markdown(f"""
                <div class="product-card">
                    <h3>{product.name}</h3>
                    <p>€{product.price:.2f}</p>
                    <p>Stock: {product.quantity}</p>
                </div>
                """, unsafe_allow_html=True)

                quantity = st.number_input(
                    "Quantity",
                    min_value=1,
                    max_value=product.quantity,
                    value=1,
                    key=f"qty_{product.name}"
                )

                if st.button("Add to Cart", key=f"add_{product.name}"):
                    st.session_state.cart.add_to_cart(product, quantity)
                    st.success(f"Added {quantity} {product.name} to cart!")
                    st.rerun()

def display_cart():
    """Display shopping cart contents"""
    st.sidebar.title("Shopping Cart")
    cart_items = st.session_state.cart.view_cart()

    if not cart_items:
        st.sidebar.info("Your cart is empty")
        return

    for item in cart_items:
        st.sidebar.markdown(f"""
        <div class="cart-item">
            <span>{item}</span>
        </div>
        """, unsafe_allow_html=True)

    total = st.session_state.cart.calculate_cart_total()
    st.sidebar.markdown(f"### Total: €{total:.2f}")

    if st.sidebar.button("Proceed to Checkout"):
        st.session_state.checkout_step = 1
        st.rerun()

def display_checkout():
    """Handle checkout process"""
    st.title("Checkout")

    progress_text = ["Shipping", "Payment", "Confirmation"]
    st.progress(st.session_state.checkout_step / len(progress_text))

    if st.session_state.checkout_step == 1:
        st.subheader("Shipping Information")
        with st.form("shipping_form"):
            st.text_input("Full Name")
            st.text_input("Address")
            st.text_input("City")
            st.text_input("Postal Code")

            if st.form_submit_button("Continue to Payment"):
                st.session_state.checkout_step = 2
                st.rerun()

    elif st.session_state.checkout_step == 2:
        st.subheader("Payment Information")
        with st.form("payment_form"):
            card_number = st.text_input("Card Number")
            col1, col2, col3 = st.columns(3)
            with col1:
                exp_month = st.number_input("Month", min_value=1, max_value=12)
            with col2:
                exp_year = st.number_input("Year", min_value=23, max_value=30)
            with col3:
                cvv = st.text_input("CVV")

            total = st.session_state.cart.calculate_cart_total()

            if st.form_submit_button(f"Pay €{total:.2f}"):
                payment = PaymentDetails(
                    card_number=card_number,
                    expiry_month=exp_month,
                    expiry_year=exp_year,
                    cvv=cvv,
                    amount=total
                )

                result = st.session_state.payment_processor.process_payment(payment)

                if result.success:
                    st.session_state.checkout_step = 3
                    st.rerun()
                else:
                    st.error(result.error_message)

    elif st.session_state.checkout_step == 3:
        st.success("Order Completed!")
        st.balloons()

        if st.button("Return to Shopping"):
            st.session_state.cart = Cart()
            st.session_state.checkout_step = 1
            st.rerun()

def main():
    st.set_page_config(
        page_title="E-Commerce Store",
        page_icon="🛍️",
        layout="wide"
    )

    apply_custom_styles()
    init_app()

    # Authentication
    if 'user' not in st.session_state:
        st.title("Welcome to Our Store")

        tab1, tab2 = st.tabs(["Login", "Register"])

        with tab1:
            username = st.text_input("Username", key="login_username")
            password = st.text_input("Password", type="password", key="login_password")

            if st.button("Login"):
                user = st.session_state.user_manager.authenticate_user(username, password)
                if user:
                    st.session_state.user = user
                    st.success("Login successful!")
                    st.rerun()
                else:
                    st.error("Invalid credentials")

        with tab2:
            new_username = st.text_input("Username", key="reg_username")
            new_password = st.text_input("Password", type="password", key="reg_password")

            if st.button("Register"):
                try:
                    st.session_state.user_manager.register_user(
                        new_username,
                        new_password,
                        UserRole.PARTNER
                    )
                    st.success("Registration successful! Please login.")
                except ValueError as e:
                    st.error(str(e))
    else:
        # Main store interface
        st.sidebar.button(
            "Logout",
            on_click=lambda: st.session_state.pop('user', None)
        )

        if st.session_state.checkout_step > 1:
            display_checkout()
        else:
            st.title("Our Products")
            display_product_grid()
            display_cart()

if __name__ == "__main__":
    main()