import pytest
from inventory_management.product import Product, NullValue, NegativeValue

def test_create_product():
	# Arrange and Act
	product = Product("1", "Test product", "test description", 100, 1)
	# Assert
	assert product.name == "Test product"
	assert product.price == 100
	assert product.quantity_in_stock == 0

def test_fail_create_name_product():
	# Arrange and Act
	with pytest.raises(ValueError) as e:
		product = Product("1", "", "test description", 100, 1)
	# Assert
	assert str(e.value) == "El nombre o la descripcion no pueden ser nulos"

def test_fail_create_description_product():
	# Arrange and Act
	with pytest.raises(ValueError) as e:
		product = Product("1", "Test product", "", 100, 1)
	# Assert
	assert str(e.value) == "El nombre o la descripcion no pueden ser nulos"

def test_fail_create_price_product():
	# Arrange and Act
	with pytest.raises() as e:
		product = Product("1", "Test product", "test description", -100, 1)
	# Assert
	assert str(e.value) == "El precio no puede ser negativo"

def test_fail_create_quantity_in_stock_product():
	# Arrange and Act
	with pytest.raises(ValueError) as e:
		product = Product("1", "Test product", "test description", 100, -1)
	# Assert
	assert str(e.value) == "La cantidad en stock no puede ser negativa"

def test_update_price():
	# Arrange
	product = Product("1", "Test product", "test description", 100, 1)
	# Act
	product.update_price(200)
	# Assert
	assert product.price == 200

def test_update_price_failure():
	# Arrange
	product = Product("1", "Test product", "test description", 100, 1)
	# Act
	with pytest.raises(NegativeValue) as e:
		product.update_price(-200)
	# Assert
	assert str(e.value) == "El precio no puede ser negativo"

def test_update_quantity_in_stock():
	# Arrange
	product = Product("1", "Test product", "test description", 100, 1)
	# Act
	product.update_quantity_in_stock(10)
	# Assert
	assert product.quantity_in_stock == 10

def test_update_quantity_in_stock_failure():
	# Arrange
	product = Product("1", "Test product", "test description", 100, 1)
	# Act
	with pytest.raises(NegativeValue) as e:
		product.update_quantity_in_stock(-10)
	# Assert
	assert str(e.value) == "La cantidad en stock no puede ser negativa"