"""
Export Manager for handling data export functionality
"""
from fpdf import FPDF
import pandas as pd
from datetime import datetime
from .inventory_manager import InventoryManager

class ExportManager:
    def __init__(self, inventory_manager: InventoryManager):
        self.inventory_manager = inventory_manager

    def export_to_pdf(self, filename: str = None) -> str:
        """Export inventory to PDF format"""
        if filename is None:
            filename = f"inventory_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"

        pdf = FPDF()
        pdf.add_page()
        
        # Title
        pdf.set_font('Arial', 'B', 16)
        pdf.cell(190, 10, 'Inventory Report', 0, 1, 'C')
        
        # Header
        pdf.set_font('Arial', 'B', 12)
        headers = ['Product', 'Price', 'Quantity', 'Total Value']
        
        # Table content
        pdf.set_font('Arial', '', 12)
        products = self.inventory_manager.get_all_products()
        
        # Calculate column widths
        col_widths = [60, 40, 40, 50]
        
        # Add headers
        for i, header in enumerate(headers):
            pdf.cell(col_widths[i], 10, header, 1)
        pdf.ln()
        
        # Add data
        for product in products:
            pdf.cell(col_widths[0], 10, str(product['name']), 1)
            pdf.cell(col_widths[1], 10, f"${product['price']:.2f}", 1)
            pdf.cell(col_widths[2], 10, str(product['quantity']), 1)
            pdf.cell(col_widths[3], 10, f"${product['total_value']:.2f}", 1)
            pdf.ln()
            
        # Add total
        total = sum(p['total_value'] for p in products)
        pdf.set_font('Arial', 'B', 12)
        pdf.cell(sum(col_widths[:3]), 10, 'Total Inventory Value:', 1)
        pdf.cell(col_widths[3], 10, f"${total:.2f}", 1)
        
        pdf.output(filename)
        return filename

    def export_to_excel(self, filename: str = None) -> str:
        """Export inventory to Excel format"""
        if filename is None:
            filename = f"inventory_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
            
        products = self.inventory_manager.get_all_products()
        df = pd.DataFrame(products)
        
        # Reorder columns
        df = df[['name', 'price', 'quantity', 'total_value']]
        
        # Rename columns
        df.columns = ['Product', 'Price', 'Quantity', 'Total Value']
        
        # Export to Excel
        df.to_excel(filename, index=False, sheet_name='Inventory')
        
        return filename
