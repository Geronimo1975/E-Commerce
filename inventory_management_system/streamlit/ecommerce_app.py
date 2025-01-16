import streamlit as st
from inventory_management_system.inventory.product import Product
from inventory_management_system.inventory.inventory_manager import InventoryManager
from inventory_management_system.inventory.user_manager import UserManager
from inventory_management_system.inventory.user import UserRole
from inventory_management_system.inventory.cart import Cart
from inventory_management_system.inventory.export_manager import ExportManager
from inventory_management_system.streamlit.payments import PaymentProcessor, PaymentDetails
from inventory_management_system.streamlit.styles import apply_custom_styles
import plotly.express as px
import pandas as pd
import logging
from functools import lru_cache

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

@st.cache_data(ttl=300)  # Cache for 5 minutes
def get_products_data(_inventory_manager):
    """Get cached products data"""
    products = _inventory_manager.get_all_products()
    return products

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

    if 'export_manager' not in st.session_state:
        st.session_state.export_manager = ExportManager(st.session_state.inventory_manager)

# Initialize the application
init_app()

# Apply custom styles
apply_custom_styles()

# Create main page layout
st.title("Starlink E-commerce Platform")

# Add tabs for different sections
tab1, tab2, tab3, tab4 = st.tabs(["Products", "Reports & Analytics", "Cart", "Product Management"])

with tab1:
    # Display products
    st.header("Available Products")

    # Get cached products data
    for product in st.session_state.inventory_manager.products:
        with st.container():
            st.markdown('<div class="product-card">', unsafe_allow_html=True)
            col1, col2, col3 = st.columns([2, 1, 1])
            with col1:
                st.write(f"### {product.name}")
                st.write(f"Price: €{product.price:.2f}")
                st.write(f"Available: {product.quantity}")
            with col2:
                quantity = st.number_input(
                    f"Quantity for {product.name}", 
                    min_value=0, 
                    max_value=product.quantity, 
                    value=0,
                    key=f"qty_{product.name}"
                )
            with col3:
                if st.button("Add to Cart", key=f"add_{product.name}") and quantity > 0:
                    st.session_state.cart.add_to_cart(product, quantity)
                    st.success(f"Added {quantity} {product.name} to cart!")
            st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    st.header("Reports & Analytics")

    # Get products data
    products_data = get_products_data(st.session_state.inventory_manager)
    df = pd.DataFrame(products_data)

    # Product Inventory Chart
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.subheader("Product Inventory Levels")
    fig_inventory = px.bar(
        df,
        x='name',
        y='quantity',
        title='Current Inventory Levels',
        labels={'name': 'Product Name', 'quantity': 'Available Units'}
    )
    st.plotly_chart(fig_inventory, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Product Value Chart
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.subheader("Product Value Distribution")
    fig_value = px.pie(
        df,
        values='total_value',
        names='name',
        title='Total Value Distribution by Product',
        hover_data=['price']
    )
    # Update hover template to show Euro symbol
    fig_value.update_traces(
        hovertemplate="<b>%{label}</b><br>Value: €%{value:.2f}<br>Price: €%{customdata[0]:.2f}<extra></extra>"
    )
    st.plotly_chart(fig_value, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Export Options
    st.subheader("Export Reports")
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Export to PDF"):
            pdf_file = st.session_state.export_manager.export_to_pdf()
            st.success(f"PDF report generated: {pdf_file}")
    with col2:
        if st.button("Export to Excel"):
            excel_file = st.session_state.export_manager.export_to_excel()
            st.success(f"Excel report generated: {excel_file}")
    st.markdown('</div>', unsafe_allow_html=True)

with tab3:
    # Display cart
    st.header("Shopping Cart")
    cart_items = st.session_state.cart.cart_items
    if not cart_items:
        st.write("Cart is empty")
    else:
        for item_name, item_data in cart_items.items():
            st.markdown('<div class="cart-item">', unsafe_allow_html=True)
            col1, col2 = st.columns([3, 1])
            with col1:
                st.write(f"{item_name} (x{item_data['quantity']}) - €{item_data['product'].price * item_data['quantity']:.2f}")
            with col2:
                if st.button("Remove", key=f"remove_{item_name}"):
                    st.session_state.cart.remove_from_cart(item_name)
                    st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

        total = st.session_state.cart.calculate_cart_total()
        st.markdown('<div class="cart-total">', unsafe_allow_html=True)
        st.write(f"Total: €{total:.2f}")
        st.markdown('</div>', unsafe_allow_html=True)

        if st.button("Proceed to Checkout"):
            st.session_state.checkout_step = 2

with tab4:
    st.header("Product Management")

    # Add new product form
    st.subheader("Add New Product")
    st.markdown('<div class="stForm">', unsafe_allow_html=True)
    with st.form("add_product_form"):
        new_product_name = st.text_input("Product Name")
        new_product_price = st.number_input("Price (€)", min_value=0.01, format="%.2f")
        new_product_quantity = st.number_input("Initial Quantity", min_value=1, value=1)

        submitted = st.form_submit_button("Add Product")
        if submitted:
            try:
                st.session_state.inventory_manager.add_product(
                    new_product_name,
                    new_product_price,
                    new_product_quantity
                )
                st.success(f"Successfully added product: {new_product_name}")
                st.rerun()  # Refresh to show the new product
            except ValueError as e:
                st.error(f"Error adding product: {str(e)}")
    st.markdown('</div>', unsafe_allow_html=True)

    # Display current inventory
    st.subheader("Current Inventory")
    products_df = pd.DataFrame(st.session_state.inventory_manager.get_all_products())
    if not products_df.empty:
        st.dataframe(
            products_df[['name', 'price', 'quantity', 'total_value']].rename(columns={
                'name': 'Product Name',
                'price': 'Price (€)',
                'quantity': 'Quantity',
                'total_value': 'Total Value (€)'
            })
        )