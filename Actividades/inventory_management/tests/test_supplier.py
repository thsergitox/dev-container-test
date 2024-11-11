import pytest

from inventory_management.supplier import Supplier

def test_create_supplier():
	# Arrange and Act
	supplier = Supplier("Supplier 1")
	# Assert
	assert supplier.name == "Supplier 1"
	assert supplier.products == []

def test_fail_create():
	pass