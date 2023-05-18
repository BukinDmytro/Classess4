class Clothing:
    def __init__(self,material, name, price,size):
        self.material = material
        self.name = name
        self.price = price
        self.size = size
class Store:
    def __init__(self,name,address):
        self.name = name
        self.address = address
        self.available = []
    def add_item(self,item):
        self.available.append(item)
    def remove_item(self,item):
        self.available.remove(item)
    def get_items(self):
        return self.available
    def search_items(self,key):
        return [item for item in self.available if key in item.name]

class Customer:
    def __init__(self,name,budget):
        self.name = name
        self.budget = budget
        self.cart = []
    def add_to_cart(self,item):
        if item.price <= self.budget:
            self.cart.append(item)
            self.budget -= item.price
            print(f"Item {item.name} was successfully added to cart")
        else:
            print("Not enough money !")
    def remove_from_cart(self,item):
        self.cart.remove(item)
    def view_cart(self):
        return self.cart
    def checkout(self):
        total_price = sum(item.price for item in self.cart)
        if total_price > self.budget:
            print("Not enough money to make a purchase (")
        else:
            self.budget -= total_price
            print(f"Authorization is successful ! Balance : {self.budget}")
            self.cart = []

shop = Store("Aber" , "Zodchih Street,2")
print(shop.name + "," + shop.address)
shop.add_item(Clothing("Polyestr" , "T-shirt" , 100 , "L"))
shop.add_item(Clothing("Cottom" , "Shirt" , 90 , "XL"))
shop.add_item(Clothing("Elastane" , "Trousers" , 210 , "M"))
print()

customer = Customer("Dima" , 190)
print(f"Customer: {customer.name} , Balance : {customer.budget}")
print()

results = shop.search_items("Shirt")
if results:
    customer.add_to_cart(results[0])
results1 = shop.search_items("T-shirt")
if results:
    customer.add_to_cart(results1[0])

customer.view_cart()
customer.remove_from_cart(results[0])
customer.remove_from_cart(results1[0])
customer.view_cart()
print()
customer.checkout()



