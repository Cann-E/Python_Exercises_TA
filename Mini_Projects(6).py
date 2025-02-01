

class Product():
    def __init__(self,name,product_id,category,price,stock):
        self.name=name
        self.product_id=product_id
        self.category=category
        self.price=price
        self.stock=stock
        
    def __str__(self):
        return f"Name: {self.name},Product Id: {self.product_id},Category: {self.category},Price: {self.price},Stock: {self.stock}"
    
    def update_stock(self,new_stock):
        print(f"{self.stock} is updated to {new_stock}")
        self.stock=new_stock
        
    def update_price(self,new_price):
        print(f"{self.price}$ has been changed to {new_price}$")
        self.price=new_price
        
    
    
class Inventory():
    def __init__(self):
        self.product_list=[]
        
    def add_product(self,product):
        self.product_list.append(product)
        print(f"{product} has been added to the inventory!")
        
    def remove_product(self,product_id):
        found=False
        for id in self.product_list:
            if id.product_id==product_id:
                self.product_list.remove(id)
                print(f"{id.name} with ID: {id.product_id} has been removed from the Inventory!")
                found=True
                break
        if not found:
            print(f"Id: {product_id},Wrong Product Id!")
            
    def view_all_products(self):
        for product in self.product_list:
            print(f"Name: {product.name},Product Id: {product.product_id},Category: {product.category},Price: {product.price},Stock: {product.stock}")
                
    def search_product(self,name):
        found=False
        for product in self.product_list:
            if product.name == name:
                print(f"Name: {product.name} has been found in the inventory with the ID: {product.product_id},Quantity: {product.stock}")
                found=True
                break
        if not found:
            print(f"Couldnt find {name} in the inventory!")
            
    def update_product_stock(self,product_id,new_stock):
        found = False 
        for id in self.product_list:
            if id.product_id == product_id:
                print(f"ProductL {id.name} stock updated to :{new_stock}")
                id.update_stock(new_stock)
                found=True
                break
        if not found:
            print(f"ID: {product_id} NOT FOUND!")
            
            
    def update_product_price(self,product_id,new_price):
        found=False
        for id in self.product_list:
            if id.product_id ==product_id:
                print(f"Product: {id.name} price has been adjusted to : {new_price}")
                id.update_price(new_price)
                found=True
                break
        if not found:
            print(f"Product ID: {product_id} Not Found!")
            
            
            
can_inventory=Inventory()


while True:
    res_1=input(
        "\nWelcome To Can Product Inventory:\n"
        "1 - Add a Product\n"
        "2 - Remove a Product\n"
        "3 - View all Products\n"
        "4 - Search for a Product\n"
        "5 - Update a Product's stock\n"
        "6 - Update a Product's price\n"
        "7 - Exit\n"
        "Enter your choice: "
    ).lower()
    
    if res_1 =="1":
        
        name=input("Please Enter Product Name: ")
        product_id=int(input("Please Enter Product ID: "))
        category=input("Please Enter Product Category: ")
        price=float(input("Please Enter Product Price: "))
        stock=int(input("Please Enter Product Stock: "))
        product=Product(name,product_id,category,price,stock)
        can_inventory.add_product(product)
    
    if res_1 =="2":
        
        product_id=int(input("Please Enter Product ID: "))
        can_inventory.remove_product(product_id)
        
    if res_1 =="3":
        
        can_inventory.view_all_products()
        
    if res_1 =="4":
        
        name=input("Please Enter Product Name: ")
        can_inventory.search_product(name)
        
    if res_1 =="5":
        
        product_id=int(input("Please Enter Product ID: "))
        new_stock=int(input("Please Enter Product's New Stock: "))
        can_inventory.update_product_stock(product_id,new_stock)
        
    if res_1 =="6":
                
        product_id=int(input("Please Enter Product ID: "))        
        new_price=float(input("Please Enter Nnew Product Price: "))        
        can_inventory.update_product_price(product_id,new_price)
        
    if res_1=="7":
        print("Thank you for Shopping With Us!")
        break
        
    
    
            
        
            
            
        
            