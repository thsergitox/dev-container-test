from product import Product
# from purchase_order import PurchaseOrder
from supplier import Supplier


class InventoryManager:

    def __init__(self):
        self.products = []
        self.suppliers = []
        self.purchase_orders = []
    

    def add_product(self, product):
        self.products.append(product)


    def remove_product(self, product_id):
        for p in self.products:
            if p.id == product_id:
                self.products.remove(p)
                return True

    def update_product(self, product):
        for p in self.products:
            if p.id == product.id:
                p = product
                return True
    
    def consult_product(self, product_id):
        for p in self.products:
            if p.id == product_id:
                return p
    
    def add_purchase_order(self, purchase_order):
        self.purchase_orders.append(purchase_order)

    def remove_purchase_order(self, purchase_order_id):
        for po in self.purchase_orders:
            if po.order_id == purchase_order_id:
                self.purchase_orders.remove(po)
                return True
    
    def update_purchase_order(self, purchase_order):
        for po in self.purchase_orders:
            if po.order_id == purchase_order.order_id:
                po = purchase_order
                return True
            
    def consult_purchase_order(self, purchase_order):
        for po in self.purchase_orders:
            if po.order_id == purchase_order.order_id:
                return True
            
    def summary(self):
        summary = ""


inventoryManager = InventoryManager()

inventoryManager.add_product(Product("1", "Test product", "test description", 100, 1))
inventoryManager.add_product(Product("2", "Test product 2", "test description 2", 200, 2))    

inventoryManager.remove_product(1)

print(inventoryManager.products)