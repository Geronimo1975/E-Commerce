import gradio as gr
import pandas as pd
import plotly.express as px
from inventory_management_system.inventory.product import Product
from inventory_management_system.inventory.inventory_manager import InventoryManager
from inventory_management_system.inventory.cart import Cart
from inventory_management_system.streamlit.payments import PaymentProcessor, PaymentDetails
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def main():
    try:
        # Initialize managers
        logger.info("Initializing application managers...")
        inventory_manager = InventoryManager()
        cart = Cart()
        payment_processor = PaymentProcessor()

        # Add initial products
        logger.info("Adding initial products...")
        for name, price, quantity in [
            ("Starlink Standard Kit", 599.00, 50),
            ("Starlink High Performance Kit", 2500.00, 25),
            ("Starlink Maritime", 5000.00, 10),
        ]:
            try:
                inventory_manager.add_product(name, price, quantity)
                logger.debug(f"Added product: {name}")
            except ValueError as e:
                logger.warning(f"Skipping product {name}: {str(e)}")

        # Create a simple interface for testing
        logger.info("Creating Gradio interface...")
        with gr.Blocks() as app:
            gr.Markdown("# Starlink E-commerce")

            # Products table
            products_df = gr.DataFrame(
                value=pd.DataFrame(inventory_manager.get_all_products()),
                headers=["Product Name", "Price (€)", "Quantity", "Total Value (€)"],
                interactive=False
            )

            # Add to cart section
            with gr.Row():
                product_name = gr.Dropdown(
                    choices=[p.name for p in inventory_manager.products],
                    label="Select Product"
                )
                quantity = gr.Number(
                    label="Quantity",
                    value=1,
                    minimum=1
                )

            status = gr.Textbox(label="Status")

            def add_to_cart(name, qty):
                try:
                    product = next((p for p in inventory_manager.products if p.name == name), None)
                    if not product:
                        return "Product not found"
                    cart.add_to_cart(product, int(qty))
                    return f"Added {qty} {name} to cart"
                except Exception as e:
                    logger.error(f"Error adding to cart: {str(e)}")
                    return f"Error: {str(e)}"

            gr.Button("Add to Cart").click(
                add_to_cart,
                inputs=[product_name, quantity],
                outputs=[status]
            )

        logger.info("Starting Gradio server...")
        app.launch(server_name="0.0.0.0", server_port=5001)
        return True

    except Exception as e:
        logger.error(f"Application startup failed: {str(e)}")
        raise

if __name__ == "__main__":
    main()