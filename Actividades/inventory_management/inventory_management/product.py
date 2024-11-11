class Product:
	id:str
	name:str
	description:str
	price:float
	quantity_in_stock:int

	def __init__(self, id:str, name:str, description:str, price:float, quantity_in_stock:int):
		if(id =="" or name == "" or description == ""):
			raise ValueError("El nombre o la descripcion no pueden ser nulos")
		self.id = id
		self.name = name
		self.description = description
		self.update_price(price)
		self.update_quantity(quantity_in_stock)

	def update_price(self, new_price:float):
		if(new_price < 0):
			raise ValueError("El precio no puede ser negativo")
		self.price = new_price
	
	def update_quantity(self, new_quantity:int):
		if(new_quantity < 0):
			raise ValueError("La cantidad no puede ser negativa")
		self.quantity_in_stock = new_quantity 

	def __repr__(self):
		return f"Product: {self.id} Precio: {self.price}, Cantidad: {self.quantity_in_stock}" 

	def summary(self):
		pass
	pass