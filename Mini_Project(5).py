

class Book():
    def __init__(self,title,book_id,author,quantity):
        self.title=title
        self.book_id=book_id
        self.author=author
        self.quantity=quantity
        
    def __str__(self):
        return f"Title: {self.title},Book Id: {self.book_id},Author: {self.author},Quantity: {self.quantity}"
    
    def update_quantity(self,new_quantity):
        self.quantity=new_quantity
        
        
class Library():
    def __init__(self):
        self.book_list=[]
        
    def add_book(self,book):
        self.book_list.append(book)
        print(f"{book} added to Library!")
        
    def remove_book(self,book_id):
        found=False
        for i in self.book_list:
            if i.book_id==book_id:
                self.book_list.remove(i)
                print(f"Title: {i.title},ID: {i.book_id} has been remove from the Library!")
                found=True
                break
        if not found:
            print(f"{book_id} Not Found in Library!")
            
    def display_books(self):
        for i in self.book_list:
            print(f"Title: {i.title},Book Id: {i.book_id},Author: {i.author},Quantity: {i.quantity}")
            
            
    def search_book(self,title):
        found=False
        for i in self.book_list:
            if i.title==title:
                print(f"Title: {i.title} has been found in the Library System!")
                found=True
                break
        if not found:
            print(f"{title} is not registered in the Library!")
            
    def update_book_quantity(self,book_id,new_quantity):
        found=False
        for i in self.book_list:
            if i.book_id==book_id:
                print(f"{i.title} quantity updated from {i.quantity} to {new_quantity}")
                i.update_quantity(new_quantity)
                found=True
                break
        if not found:
            print(f"Id: {book_id} Not Found!")
            
            
            
Can_Library=Library()


while True:
    res_1 = input(
        "\nWelcome To Can Library:\n"
        "1 - Add a Book\n"
        "2 - Remove a Book\n"
        "3 - View all Books\n"
        "4 - Search for a Book\n"
        "5 - Update a Book's Quantity\n"
        "6 - Exit\n"
        "Enter your choice: "
    ).lower()
    
    if res_1 =="1":
        title=input("Please Enter Title: ")
        author=input("Please Enter Author: ")
        book_id=int(input("Please Enter Book ID: "))
        quantity=int(input("Please Enter Quantity: "))
        book_1=Book(title,book_id,author,quantity)
        Can_Library.add_book(book_1)
        
    elif res_1 =="2":
        book_id=int(input("Please Enter Book ID: "))
        Can_Library.remove_book(book_id)
        
    elif res_1 =="3":
        Can_Library.display_books()
    
    elif res_1 =="4":
        title=input("Please Enter Title: ")
        Can_Library.search_book(title)
        
    elif res_1 =="5":        
        book_id=int(input("Please Enter Book ID: "))
        new_quantity=int(input("Please Enter Quantity: "))
        
        Can_Library.update_book_quantity(book_id,new_quantity)
        
    elif res_1=="6":
        print("Thank you for Visiting Can's Library !")
        break
    
        