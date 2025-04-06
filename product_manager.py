
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

## metoda pentru a elimina produsele dupa nume:   
    def remove_product_by_name(self, product_name):
        found = False
        for product in self.products:
            if product.name.lower() == product_name.lower():
                self.products.remove(product)
                print(f"\n Produsul '{product_name}' a fost eliminat cu succes.")
                found = True
                break
        if not found:
            print(f"Produsul '{product_name}' nu a fost găsit.")