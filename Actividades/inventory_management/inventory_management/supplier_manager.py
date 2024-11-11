
class SupplierManager():
    suppliers: list

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SupplierManager, cls).__new__(cls)
            cls.instance.suppliers = []
            
    def __init__(self):
        # 
        pass

    def add_supplier(self, supplier):
        self.suppliers.append(supplier)
    
    def remove_supplier(self, supplier_id):
        [s for s in self.suppliers if s.id != supplier_id]
        
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
        """
        Consults a supplier by its id
        Output: Supplier object or None
        """
        for s in self.suppliers:
            if s.id == supplier_id:
                return s
        return None
    