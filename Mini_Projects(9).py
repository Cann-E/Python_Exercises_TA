

class Book():
    def __init__(self,title,book_id,author,genre,is_borrowed=False,borrower=None,return_date=None):
        self.title=title
        self.book_id=book_id
        self.author=author
        self.genre=genre
        self.is_borrowed=is_borrowed
        self.borrower=borrower
        self.return_date=return_date
        
    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        borrower_info = f", Borrower: {self.borrower}, Return Date: {self.return_date}" if self.is_borrowed else ""
        return f"Title: {self.title}, ID: {self.book_id}, Author: {self.author}, Genre: {self.genre}, Status: {status}{borrower_info}"

    
    def borrow_book(self,borrower_name,return_date):
        if self.is_borrowed == False:
            print(f"Book borrowed by {borrower_name} and return date is : {return_date}")
            self.borrower=borrower_name
            self.return_date=return_date
            self.is_borrowed = True
        else:
            print("Book is already taken out!")
            
    def return_book(self):
        if self.is_borrowed:
            print(f"Book has been Returned!")
            self.is_borrowed = False
            self.borrower = None  
            self.return_date = None  
        else:
            print("Book is already in the system!")

            
    def update_genre(self,new_genre):
        old_genre=self.genre
        self.genre=new_genre
        print(f"Genre change! Old Genre: {old_genre} to {new_genre}")
        
        
class Library():
    def __init__(self):
        self.book_list=[]
        
    def add_book(self,book):
        self.book_list.append(book)
        print(f"{book} added to System!")
        
    def remove_book(self,book_id):
        found = False
        for id in self.book_list:
            if id.book_id == book_id:
                self.book_list.remove(id)
                print(f"Book Removed! {id.title}")
                found = True
                break
        if not found:
            print(f"ID: {id},Book not Found!")
            
    def display_books(self):
        for book in self.book_list:
            print(f"Title: {book.title}, ID: {book.book_id}, Author: {book.author}, Genre: {book.genre}")
            
    def search_book(self,title):
        found = False
        for title_ in self.book_list:
            if title_.title== title:
                print(f"Title: {title_.title},Book Found!")
                found = True
                break
        if not found:
            print(f"{title_.title} not found!")
            
    def borrow_book_(self,book_id,borrower_name,return_date):
        found = False
        for id in self.book_list:
            if id.book_id == book_id:
                print("Book Borrowed!")
                id.borrow_book(borrower_name,return_date)
                found = True
                break
        if not found:
            print(f"ID: {book_id} not match any book!")
            
    def return_book_(self,book_id):
        found = False
        for id in self.book_list:
            if id.book_id == book_id:
                print(f"Book Returned!")
                id.return_book()
                found = True
                break
        if not found:
            print("Cant Return the book!")
            
    def sort_books_by_title(self):
        self.book_list.sort(key=lambda book: book.title)
        print("Books are sorted!")
        for books in self.book_list:
            print(books)
            
    def filter_books_by_genre(self,genre):
        filtered_list=list(filter(lambda book: book.genre==genre,self.book_list))
        if filtered_list:
            print(f"Book Genre in:{genre}")
            for book in filtered_list:
                print({book})
            else:
                print(f"No book found in {genre}")
                
    def track_overdue_books(self, current_date):
        overdue_list = list(filter(lambda book: book.return_date is not None and book.return_date < current_date, self.book_list))

        if overdue_list:
            print("Overdue Books:")
            for book in overdue_list:
                print(f"Title: {book.title}, Borrower: {book.borrower}, Due Date: {book.return_date}")
        else:
            print("No overdue books found.")
            
            
can_library=Library()

while True:
    res1=input(
        "\nWelcome To Library:\n"
"1 - Add a book\n"
"2 - Remove a book\n"
"3 - View all books\n"
"4 - Search for a book\n"
"5 - Borrow a book\n"
"6 - Return a book\n"
"7 - Sort books by title\n"
"8 - Filter books by genre\n"
"9 - Track overdue books\n"
"10 - Exit\n"
"Enter your choice: "

    ).lower()
    
    if res1 == "1":
        title = input("Enter Book Title: ")
        book_id = input("Enter Book ID: ")
        author = input("Enter Author Name: ")
        genre = input("Enter Book Genre: ")
        is_borrowed = False  
        borrower = None  
        return_date = None  
        book = Book(title, book_id, author, genre, is_borrowed, borrower, return_date)
        can_library.add_book(book)
        
    if res1 == "2":
        book_id = input("Enter Book ID: ")
        can_library.remove_book(book_id)
        
    if res1 == "3":
        can_library.display_books()
        
    if res1 == "4":
        title = input("Enter Book Title: ")
        can_library.search_book(title)
        
    if res1 == "5":
        book_id = input("Enter Book ID: ")
        borrower_name=input("Please Enter Borrower Name: ")
        return_date=input("Please enter Return Date: ")
        can_library.borrow_book_(book_id,borrower_name,return_date)
        
    if res1 == "6":
        book_id = input("Enter Book ID: ")
        can_library.return_book_(book_id)
        
    if res1 == "7":
        can_library.sort_books_by_title()
        
    if res1 == "8":
        filter_genre = input("Enter Book Genre for Filtering: ")
        can_library.filter_books_by_genre(filter_genre)
        
    if res1 == "9":
        track_overdue = input("Please Enter Current Date to Track Overdues:  ")
        can_library.track_overdue_books(track_overdue)
        
    if res1 == "10":
        print("Thank you for visiting Cans Library!")
        break
        
        
        
        

        

        
            
            
        
        