from product import Product
# from inventory_management import inventory_manager

class Supplier:
    def __init__(self, id, name, contact_info, products_supplied):
        self.id = id
        if name == "":
            raise ValueError("Name is required")
        self.name = name
        if contact_info == "":
            raise ValueError("Contact info is required")
        self.contact_info = contact_info
        if not products_supplied:
            raise ValueError("Products supplied is required")
        if not all((product.id) for product in products_supplied):
            raise ValueError("Products supplied must be a list of Product instances")
        self.products_supplied = products_supplied

    def add_product(self, product):
        if isinstance(product, Product):
            self.products_supplied.append(product)

    def remove_product(self, product_id):
        self.products_supplied = [product for product in self.products_supplied if product.id != product_id]

    def summary(self):
        return f"Supplier {self.name} with id {self.id} supplies {len(self.products_supplied)} products"