from supplier import Supplier
from product import Product
from inventory_management import inventory_manager
from supplier_manager import supplier_manager
class PurchaseOrder():
    order_id: int
    supplier: Supplier
    order_items: list[Product]
    status: str                 # pendiente, completada, cancelada

    def __init__(self, order_id, supplier):
        assert isinstance(supplier, Supplier) # The provider has to exists
        self.order_id = order_id
        self.supplier = supplier
        self.order_items = []
        self.status = "pendiente"
    
    def create_order(self, supplier_id, order_items):
        """
        Creates a new purchase order validating the items are in stock
        """
        # Search the supplier
        supplier = supplier_manager(supplier_id)
        if supplier is None:
            
            return "Proveedor no encontrado"

        # Validating the items are in stock
        for item in order_items:
            if inventory_manager.consult(item.id) == False:
                return "Item fuera de stock"

        # Creating the purchase order
        inventory_manager.remove_items(order_items)
        self.order_items = order_items
        self.update_status("completada")

    def update_status(self, new_status):
        """
        Updates the status of the purchase order
        """
        self.status = new_status
    
    def summary(self):
        """
        Returns a summary of the purchase order
        """
        summary_str = f"Purchase order {self.order_id} with {len(self.order_items)} items from {self.supplier.name} is {self.status}"
        summary_str += "\nItems:"
        for item in self.order_items:
            summary_str += f"\n{item.name} - {item.quantity} units"

        return summary_str
        
