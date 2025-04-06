
from product import Product
from product_manager import ProductManager

pm = ProductManager()
pm.add_products(Product("Laptop", 3500, 5))
pm.add_products(Product("Smartphone", 2000, 20))
pm.add_products(Product("Tablet", 1500, 15))

pm.show_all_products()  ##-afisarea tuturor produselor

total_inventory = pm.show_total_inventory()             ##-apelarea metodei inventar
print(f"Total inventory value is {total_inventory}")    ##-afisarea valorii inventarului total


    