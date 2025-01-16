class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity

    def get_product_info(self):
        # Format price with two decimals
        return f"Product: {self.name}, Price: {self.price:.2f}€, Quantity: {self.quantity}"
