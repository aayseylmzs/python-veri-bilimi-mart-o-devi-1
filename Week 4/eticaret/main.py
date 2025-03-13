#from product import Product
#from customer import Customer
#from cart import Cart
#from order import Order

#def main():

   # products = [
   #     Product("Laptop",15000,5),
   #     Product("Telefon",10000,15),
   #     Product("Kulaklık",500,150)
   # ]

#from product import Product
#from customer import Customer
#from cart import Cart
#from order import Order

def main():
    # Ürünleri oluşturuyoruz
    products = [
        Product("Laptop", 15000, 5),
        Product("Telefon", 10000, 15),
        Product("Kulaklık", 500, 150)
    ]
    
    # Müşteri oluşturuyoruz
    customer = Customer("Ayşe", "ayse@example.com")
    
    # Sepet oluşturuyoruz
    cart = Cart()
    
    # Sepete ürün ekliyoruz
    cart.add_product(products[0], 2)  # 2 Laptop
    cart.add_product(products[1], 1)  # 1 Telefon
    
    # Sipariş oluşturuyoruz
    order = Order(customer, cart)
    order.place_order()

if __name__ == "__main__":
    main()













if __name__ == "__main__":
    main()