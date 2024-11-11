import pytest
import inventory_management.supplier as sup
import inventory_management.purchase_order as po
import inventory_management.product as pr

def test_create_purchase_order():
    # ARRANGE
    
    # Create products from the supplier
    products = []
    products.append(pr.Product(1, "Laptop","A gaming laptop", 1000, 10))
    products.append(pr.Product(2, "Mouse", "A gaming mouse", 20, 100))

    # Create supplier
    test_supplier = sup.Supplier(1, "Andrew", "Honorio Delgado", products)

    # Create products to order
    products_to_order = set()
    products_to_order.add(pr.Product(1, "Laptop","A gaming laptop", 1000, 5))

    # Create purchase order
    purchase_order = po.PurchaseOrder(1, test_supplier, products_to_order)

    # ACT
    po.create_purchase_order(test_supplier, products_to_order)

    # ASSERT
    assert po.purchase_orders[1] == 10
