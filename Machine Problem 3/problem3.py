# Challenge 1:The Book Blueprint (Class) 
"""
* Create a python class named Book 
* It should have an __init__ method that accepts title, author, and isbn as arguments and store them as attributes
* It should also have a __str__ method that returns a nicely formatted string represnting the book.
For ex: "The Hobbit by J.R.R. Tolkien (ISBN: 12345)"
"""

# Challenged 2: The ebook specialty (inheritance)

"""
* Create a new class named Ebook that inherits from your book class 
* In addition to the attributes from book, the Ebook class should also have a file_format attribute (e.g., 'PDF','EPUB')
* The __init__ method should accept title, author, isbn, and file_format.
* Override the __str__ method to include the file format in the output. 
For ex: "Dune by Frank Herbert (ISBN: 67890) - Format: EPUB" 
"""

# Challeenge 3: The library collection (Iterator)
"""
* Create a class named library
* The __init__ method should initialize an empty list to hold book objects 
* create a method add_book(self, book) that adds a Book or Ebook object to this list 
* Make the library class iterable. This means you need to implement the iterator protocol 
(__iter__ and __next__) so you can loop through the books in the library directly using a for loop
"""



# Challenge 1: The Book Blueprint (Class)
class Book: 
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
    
    def inputDetails(self):
        while True:
            self.title = input("Enter Book Title: ")
            if self.title.strip() == "":
                print("Title cannot be empty. Please try again.")
                continue
            self.author = input("Enter Book Author: ")
            if self.author.strip() == "":
                print("Author cannot be empty. Please try again.")
                continue
            self.isbn = input("Enter Book ISBN: ")
            if self.isbn.strip() == "":
                print("ISBN cannot be empty. Please try again.")
                continue
            break

    def __str__(self): 
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"



# Challenge 2: The Ebook Specialty (Inheritance)
class Ebook(Book): 
    def __init__(self, title, author, isbn, file_format): 
        super().__init__(title, author, isbn)
        self.file_format = file_format

    def inputDetails(self):
        super().inputDetails()
        while True: 
            self.file_format = input("Enter ebook file format: ")
            if self.file_format.strip() == "":
                print("File format cannot be empty. Please try again.")
                continue
            break

    def __str__(self): 
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - Format: {self.file_format}"



# Challenge 3: The Library Collection (Iterator)
class Library: 
    def __init__(self):
        self.books = []
    
    def add_book(self, book): 
        self.books.append(book)

    def __iter__(self):
        return iter(self.books)

    def __next__(self):
        if not self.books:
            raise StopIteration
        return self.books.pop(0)

def main(): 
    while True: 
        choice = input("What problem do you want to try? (1, 2 ,3, or q to quit):")

        if choice == '1': 
            b = Book("", "", "")
            b.inputDetails()
            print(b)

        elif choice == '2':
            test = Ebook("", "", "", "")
            test.inputDetails()
            print(test)

        elif choice == '3':
            lib = Library()

            count = int(input("How many books do you want to add? "))
            for i in range(count):
                book_type = input("Is it a physical book or an ebook? (p/e): ").lower()
                while True: 
                    title = input("Enter book title: ")
                    if title.strip() == "": 
                        print("Title cannot be empty. Please try again.")
                        continue
                    author = input("Enter book author: ")
                    if author.strip() == "": 
                        print("Author cannot be empty. Please try again.")
                        continue
                    isbn = input("Enter book ISBN: ")
                    if isbn.strip() == "": 
                        print("ISBN cannot be empty. Please try again.")
                        continue
                    break
                if book_type == 'e':
                    while True: 
                        file_format = input("Enter ebook file format: ")
                        if file_format.strip() == "": 
                            print("File format cannot be empty. Please try again.")
                            continue
                        break
                    book = Ebook(title, author, isbn, file_format)
                else:
                    book = Book(title, author, isbn)
                lib.add_book(book)

            print("\nBooks in the library:")
            for book in lib:
                print(book, "\n\n")

        elif choice == 'q':
            break

        else: 
            print("Invalid choice. Please try again.")

if __name__ == "__main__": 
    main()