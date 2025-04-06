
## Definirea clasei Cart
from product import Product
from product_manager import ProductManager

class Cart:
    def __init__(self):
        self.cart_items = []
    
    def add_to_cart(self, product):
        self.cart_items.append(product)    

    def cart_total_value(self):
        return sum(product.price * product.quantity for product in self.cart_items)
    
    def show_all_cart(self):
       for items in self.cart_items:
            print(items.display_product())
