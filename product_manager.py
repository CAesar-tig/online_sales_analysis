
## Definirea clasei Product Manager

##a. import class Product:
from product import Product


##b. class Product Manager: 
class ProductManager:
    def __init__(self):
        self.products = []
        
    def add_products(self, product):
        self.products.append(product)
        
    def show_all_products(self):
       for product in self.products:
            print(product.display_product()) 

    def show_total_inventory(self):
        return sum(product.price * product.quantity for product in self.products)
      