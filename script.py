"""
Utility script for the E-commerce Platform
This script can be used for various maintenance tasks and data operations
"""
from inventory_management_system.inventory.inventory_manager import InventoryManager
from inventory_management_system.inventory.export_manager import ExportManager

def main():
    """Main function to handle utility operations"""
    inventory_manager = InventoryManager()
    export_manager = ExportManager(inventory_manager)
    
    # Add some sample products
    inventory_manager.add_product("Starlink Standard Kit", 599.00, 50)
    inventory_manager.add_product("Starlink High Performance Kit", 2500.00, 25)
    
    # Export sample reports
    export_manager.export_to_pdf("inventory_report.pdf")
    export_manager.export_to_excel("inventory_report.xlsx")

if __name__ == "__main__":
    main()
