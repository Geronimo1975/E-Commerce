import streamlit as st
from inventory.product import Product
from inventory.inventory_manager import InventoryManager
from inventory.cart import Cart
from inventory.export_manager import ExportManager

LIGHT_THEME = """
<style>
div[data-testid="stAppViewContainer"] {
    background-color: #FFFFFF !important;
    color: #000000 !important;
}
</style>
"""

DARK_THEME = """
<style>
div[data-testid="stAppViewContainer"] {
    background-color: #262730 !important;
    color: #FFFFFF !important;
}
</style>
"""

def init_data():
    """Initializes an InventoryManager, creates some sample products, and returns both the manager and a Cart object."""
    inventory_manager = InventoryManager()
    cart = Cart()
    
    # Create a few test products
    inventory_manager.add_product("Laptop", 1000.00, 5)
    inventory_manager.add_product("Smartphone", 500.00, 10)
    
    return inventory_manager, cart

def main():
    st.title("Simple Inventory Management System")
    
    theme_choice = st.radio("Select Theme:", ["Light", "Dark"])
    if theme_choice == "Light":
        st.markdown(LIGHT_THEME, unsafe_allow_html=True)
    else:
        st.markdown(DARK_THEME, unsafe_allow_html=True)

    # Initialize data
    if "inventory_manager" not in st.session_state:
        st.session_state["inventory_manager"], st.session_state["cart"] = init_data()
    
    inventory_manager = st.session_state["inventory_manager"]
    cart = st.session_state["cart"]
    
    # Section to add products to the inventory
    st.subheader("Add Products to Inventory")
    product_name = st.text_input("Product Name:", "")
    product_price = st.number_input("Product Price:", value=0.0, step=0.01)
    product_quantity = st.number_input("Product Quantity:", value=0, step=1)
    
    if st.button("Add Product"):
        if product_name and product_price > 0 and product_quantity > 0:
            inventory_manager.add_product(product_name, product_price, product_quantity)
            st.success(f"Product '{product_name}' has been added to the inventory!")
        else:
            st.warning("Please enter a valid name, a price > 0, and a quantity > 0.")
    
    st.write("---")
    
    # Display the current list of products
    st.subheader("Current Inventory:")
    products = inventory_manager.get_all_products()
    if products:
        for prod in products:
            st.write(prod)
    else:
        st.write("The inventory is empty.")
    
if __name__ == "__main__":
    main()