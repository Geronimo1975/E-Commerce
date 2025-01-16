"""
Streamlit interface for the Inventory Management System.
"""
import os
import sys
import logging
from datetime import datetime
from collections import deque

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
    ]
)
logger = logging.getLogger(__name__)

# Import streamlit
try:
    import streamlit as st
except ImportError as e:
    logger.error(f"Failed to import Streamlit: {str(e)}")
    sys.exit(1)

# Set page config
st.set_page_config(
    page_title="Inventory Management System",
    page_icon="🏪",
    layout="wide"
)

# Import application modules
try:
    from inventory.database import test_database_connection
    from inventory.inventory_manager import InventoryManager
    from inventory.user import UserRole
    from inventory.user_manager import UserManager
    logger.info("Application modules imported successfully")
except ImportError as e:
    error_msg = f"Failed to import application modules: {str(e)}"
    logger.error(error_msg)
    st.error(error_msg)
    sys.exit(1)

# Initialize session state
if 'initialized' not in st.session_state:
    st.session_state.initialized = False
    st.session_state.current_user = None
    st.session_state.inventory = None
    st.session_state.user_manager = None
    logger.info("Session state initialized")

def main():
    """Main application entry point."""
    try:
        # Check database connection
        if not test_database_connection():
            st.error("Database connection failed. Please check your configuration.")
            return

        # Initialize managers
        if not st.session_state.user_manager:
            try:
                st.session_state.user_manager = UserManager()
            except Exception as e:
                st.error(f"Failed to initialize user management: {str(e)}")
                return

        if not st.session_state.inventory:
            try:
                st.session_state.inventory = InventoryManager()
            except Exception as e:
                st.error(f"Failed to initialize inventory management: {str(e)}")
                return

        # Display login page if not logged in
        if not st.session_state.current_user:
            st.title("🏪 Inventory Management System")
            st.header("Login")

            username = st.text_input("Username")
            password = st.text_input("Password", type="password")

            if st.button("Login"):
                user = st.session_state.user_manager.authenticate_user(username, password)
                if user:
                    st.session_state.current_user = user
                    st.success("Login successful!")
                    st.rerun()
                else:
                    st.error("Invalid username or password")
        else:
            # Display main inventory page
            st.title("🏪 Inventory Management")

            # User info and logout
            col1, col2 = st.columns([3, 1])
            with col1:
                st.write(f"Welcome, {st.session_state.current_user.username}")
            with col2:
                if st.button("Logout"):
                    st.session_state.current_user = None
                    st.rerun()

            # Display inventory content
            if st.session_state.inventory:
                total_value = st.session_state.inventory.get_total_inventory_value()
                st.metric("Total Inventory Value", f"${total_value:.2f}")

                products = st.session_state.inventory.get_all_products()
                if products:
                    for product in products:
                        with st.expander(f"{product['name']} - ${product['price']:.2f}"):
                            st.write(f"Quantity: {product['quantity']}")
                            st.write(f"Total Value: ${product['total_value']:.2f}")

                            if st.session_state.current_user.role == UserRole.ADMIN:
                                new_qty = st.number_input(
                                    "New Quantity",
                                    min_value=0,
                                    value=product['quantity'],
                                    key=f"qty_{product['name']}"
                                )
                                if st.button("Update", key=f"update_{product['name']}"):
                                    try:
                                        st.session_state.inventory.update_quantity(
                                            product['name'],
                                            new_qty
                                        )
                                        st.success(f"Updated {product['name']} quantity to {new_qty}")
                                        st.rerun()
                                    except Exception as e:
                                        st.error(str(e))
                else:
                    st.info("No products in inventory")
            else:
                st.error("Inventory manager not initialized")

    except Exception as e:
        logger.error(f"Application error: {str(e)}")
        st.error("An unexpected error occurred. Please try again.")

if __name__ == "__main__":
    main()