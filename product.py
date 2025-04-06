
## Definirea clasei Product
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def display_product(self):
        return f"Product name: {self.name} with Price: {self.price} and Quantity: {self.quantity}"
        
    def update_quantity(self, amount):
        if self.quantity > 0:
            self.quantity += amount
        else:
            print(f"Quantity for Product {self.name} cannot be 0 or negative") 