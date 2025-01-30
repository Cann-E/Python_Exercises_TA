

class Book():
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn  # Fixed typo (self,isbn-isbn → self.isbn = isbn)
        self.available = True  # Default should be True (available)

class Library():
    def __init__(self):
        self.library_ = []  # List to store Book objects

    def add_book(self, book):
        self.library_.append(book)
        print(f"'{book.title}' has been added to the library.")

    def remove_book(self, isbn):
        for book in self.library_: #checks each element in the list
            if book.isbn == isbn:  #if the book number thats currently in the lists matches with the argument number
                self.library_.remove(book) #remove the book with the associated identifier from the library
                print(f"Book with ISBN {isbn} has been removed.")
                return
        print("Book not found!")

    def display_books(self):
        print("Books in Library:")
        if not self.library_:
            print("No books in the library.")
        for book in self.library_:
            print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}, Available: {book.available}")

    def search_book(self, title):
        found = False
        for book in self.library_: #checks each element in the list
            if book.title.lower() == title.lower():  #if eleemnt title matches the argument title
                print(f"'{book.title}' is found in the library!")
                found = True
                break
        if not found:
            print(f"'{title}' not FOUND!")

    def borrow_book(self, isbn):
        for book in self.library_:  #checks each element in the list
            if book.isbn == isbn:   #if the book number thats currently in the lists matches with the argument number
                if book.available:  #if the book available is True meaning its inside the list
                    book.available = False  #change book status to unavailable meaning False
                    print(f"You have borrowed '{book.title}'.")
                else:
                    print("Book is already borrowed!")
                return
        print("Book not found!")

    def return_book(self, isbn):
        for book in self.library_: #checks each element in the list
            if book.isbn == isbn:   #if the book number thats currently in the lists matches with the argument number
                if not book.available:  #than check if book is already checked out
                    book.available = True #return the status of the book to available
                    print(f"'{book.title}' has been returned to the library.")
                else:
                    print("Book is already available in the library.")
                return
        print("Book not found!")

# ✅ **Testing the Corrected Library Management System**
my_library = Library()

book1 = Book("Harry Potter", "J.K. Rowling", "15789")
book2 = Book("The Great Gatsby", "F. Scott Fitzgerald", "24680")
book3 = Book("1984", "George Orwell", "13579")

# ✅ Add books
my_library.add_book(book1)
my_library.add_book(book2)
my_library.add_book(book3)

# ✅ Display books
my_library.display_books()

# ✅ Search for a book
my_library.search_book("1984")

# ✅ Borrow a book
my_library.borrow_book("15789")
my_library.display_books()

# ✅ Try to borrow the same book again
my_library.borrow_book("15789")

# ✅ Return a book
my_library.return_book("15789")
my_library.display_books()

# ✅ Remove a book
my_library.remove_book("24680")
my_library.display_books()
