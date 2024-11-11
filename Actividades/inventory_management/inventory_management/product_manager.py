class ProductManager:
    
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
    
        def add_supplier(self, supplier):
            self.suppliers.append(supplier)
    
        def remove_supplier(self, supplier_id):
            for s in self.suppliers:
                if s.id == supplier_id:
                    self.suppliers.remove(s)
                    return True
    
        def update_supplier(self, supplier):
            for s in self.suppliers:
                if s.id == supplier.id:
                    s = supplier
                    return True
    
        def consult_supplier(self, supplier_id):
            for s in self.suppliers:
                if s.id == supplier_id:
                    return s
    
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
            return summary
