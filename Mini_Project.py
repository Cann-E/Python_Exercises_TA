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
        for book in self.library_:
            if book.isbn == isbn:
                self.library_.remove(book)
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
        for book in self.library_:
            if book.title.lower() == title.lower():  # Case-insensitive search
                print(f"'{book.title}' is found in the library!")
                found = True
                break
        if not found:
            print(f"'{title}' not FOUND!")

    def borrow_book(self, isbn):
        for book in self.library_:
            if book.isbn == isbn:
                if book.available:
                    book.available = False
                    print(f"You have borrowed '{book.title}'.")
                else:
                    print("Book is already borrowed!")
                return
        print("Book not found!")

    def return_book(self, isbn):
        for book in self.library_:
            if book.isbn == isbn:
                if not book.available:
                    book.available = True
                    print(f"'{book.title}' has been returned to the library.")
                else:
                    print("Book is already available in the library.")
                return
        print("Book not found!")

# ✅ **Testing with Minimal Fixes**
library = Library()

book1 = Book("Harry Potter", "J.K. Rowling", "15789")
library.add_book(book1)

library.display_books()
library.search_book("Harry Potter")
library.borrow_book("15789")
library.display_books()
library.return_book("15789")
library.display_books()
