
from product import Product
from product_manager import ProductManager
from cart import Cart

pm = ProductManager()                                   ##- instanta Product Manager
pm.add_products(Product("Laptop", 3500, 5))
pm.add_products(Product("Smartphone", 2000, 20))
pm.add_products(Product("Tablet", 1500, 15))

print("\n Products selection  is:")
pm.show_all_products()  ##-afisarea tuturor produselor

total_inventory = pm.show_total_inventory()             ##-apelarea metodei inventar
print(f"Total inventory value is {total_inventory:.2f}")    ##-afisarea valorii inventarului total

cart = Cart()
cart.add_to_cart(Product("Laptop", 3500, 1))
cart.add_to_cart(Product("Smartphone", 2000, 1))
cart.add_to_cart(Product("Smartphone", 2000, 1))

cart_value = cart.cart_total_value()
print(f"\nCart total value is {cart_value:.2f}") 
print(" Products added to cart are:")
cart.show_all_cart()


