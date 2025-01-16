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

        with gr.Blocks(theme=gr.themes.Default()) as app:
            with gr.Row():
                with gr.Column(scale=1):
                    gr.Markdown("## Product Configuration")

                    with gr.Group():
                        product_name = gr.Dropdown(
                            choices=[p.name for p in inventory_manager.products],
                            label="Select Product",
                            info="Choose a Starlink product"
                        )

                        quantity = gr.Slider(
                            minimum=1,
                            maximum=10,
                            step=1,
                            value=1,
                            label="Quantity"
                        )

                    with gr.Accordion("Advanced Options", open=False):
                        shipping_method = gr.Radio(
                            choices=["Standard", "Express", "Priority"],
                            value="Standard",
                            label="Shipping Method"
                        )
                        installation = gr.Checkbox(
                            label="Include Professional Installation",
                            value=False
                        )

                    add_to_cart_btn = gr.Button(
                        "Add to Cart",
                        variant="primary"
                    )
                    status = gr.Textbox(
                        label="Status",
                        interactive=False
                    )

                with gr.Column(scale=2):
                    with gr.Tab("Products"):
                        products_df = gr.DataFrame(
                            value=pd.DataFrame(inventory_manager.get_all_products()),
                            headers=["Product Name", "Price (€)", "Quantity", "Total Value (€)"],
                            interactive=False
                        )

                        with gr.Row():
                            inventory_plot = gr.Plot(label="Inventory Levels")
                            value_plot = gr.Plot(label="Value Distribution")

                        refresh_btn = gr.Button("Refresh Analytics")

                    with gr.Tab("Cart"):
                        cart_contents = gr.TextArea(
                            label="Cart Contents",
                            interactive=False,
                            lines=5
                        )
                        cart_total = gr.Textbox(
                            label="Total",
                            interactive=False
                        )

                        with gr.Group():
                            gr.Markdown("### Payment Details")
                            with gr.Row():
                                with gr.Column(scale=1):
                                    card_number = gr.Textbox(
                                        label="Card Number",
                                        max_lines=1
                                    )
                                    exp_month = gr.Number(
                                        label="Expiry Month",
                                        minimum=1,
                                        maximum=12
                                    )
                                with gr.Column(scale=1):
                                    exp_year = gr.Number(
                                        label="Expiry Year",
                                        minimum=datetime.now().year % 100
                                    )
                                    cvv = gr.Textbox(
                                        label="CVV",
                                        max_lines=1
                                    )

                            process_payment_btn = gr.Button(
                                "Process Payment",
                                variant="primary"
                            )
                            payment_status = gr.Textbox(
                                label="Payment Status",
                                interactive=False
                            )

            def add_to_cart(name, qty, shipping, install):
                try:
                    product = next((p for p in inventory_manager.products if p.name == name), None)
                    if not product:
                        return "Product not found"

                    cart.add_to_cart(product, int(qty))
                    extras = []
                    if shipping != "Standard":
                        extras.append(shipping)
                    if install:
                        extras.append("Professional Installation")

                    return f"Added {qty} {name} to cart" + (f" with {', '.join(extras)}" if extras else "")
                except Exception as e:
                    logger.error(f"Error adding to cart: {str(e)}")
                    return f"Error: {str(e)}"

            def update_cart_view():
                try:
                    items = cart.cart_items
                    if not items:
                        return "Cart is empty", "€0.00"

                    cart_text = "\n".join([
                        f"{name}: {data['quantity']} x €{data['product'].price:.2f}"
                        for name, data in items.items()
                    ])
                    total = cart.calculate_cart_total()
                    return cart_text, f"€{total:.2f}"
                except Exception as e:
                    logger.error(f"Error updating cart view: {str(e)}")
                    return "Error viewing cart", "Error"

            def update_analytics():
                try:
                    df = pd.DataFrame(inventory_manager.get_all_products())

                    fig_inventory = px.bar(
                        df,
                        x='name',
                        y='quantity',
                        title='Current Inventory Levels'
                    )

                    fig_value = px.pie(
                        df,
                        values='total_value',
                        names='name',
                        title='Product Value Distribution'
                    )

                    return fig_inventory, fig_value
                except Exception as e:
                    logger.error(f"Error updating analytics: {str(e)}")
                    return None, None

            # Event handlers
            add_to_cart_btn.click(
                add_to_cart,
                inputs=[product_name, quantity, shipping_method, installation],
                outputs=[status]
            )

            refresh_btn.click(
                update_analytics,
                outputs=[inventory_plot, value_plot]
            )

            # Initialize displays
            update_analytics()

        logger.info("Starting Gradio server...")
        app.launch(server_name="0.0.0.0", server_port=5001)
        return True

    except Exception as e:
        logger.error(f"Application startup failed: {str(e)}")
        raise

if __name__ == "__main__":
    main()