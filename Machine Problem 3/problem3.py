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
    
    def __str__(self): 
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"


b1 = Book("The Hobbit", "J.R.R. Tolkien", "12345")
print("Chellenge 1 results:",b1)


# Challenge 2: The Ebook Specialty (Inheritance)
class Ebook(Book): 
    def __init__(self, title, author, isbn, file_format): 
        super().__init__(title, author, isbn)
        self.file_format = file_format

    def __str__(self): 
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - Format: {self.file_format}"

test = Ebook("Dune", "Frank Herbert", "67890", "EPUB")

print("\n\nChellenge 2 results:", test)


# Challenge 3: The Library Collection (Iterator)
class Library: 
    def __init__(self):
        self.books = []
    
    def add_book(self, book): 
        self.books.append(book)

    def __iter__(self): 
        self.a = 0
        return self 

    def __next__(self):
        if self.a < len(self.books):
            # if you only did this it will be index out of range 
            """
            because the __next__ method tried to access self.books[self.a] when self.a might be equal or greater than the length of self.books
            each time you access next(), self,a increases by 1 
            so when you reach the length of self.books there are no mo items left but still try to access self.books[self.books]
            """
            x = self.books[self.a]
            self.a += 1
            return x 
        else: 
            raise StopIteration
        
lib = Library() 
libIter = iter(lib)

for i in range(5): 
    if i % 2 == 0: 
        lib.add_book(f"book {i} - author {i} (ISBN: {i*123})")
    else: 
        lib.add_book(f"book {i} - author {i} (ISBN: {i*123})")

print("\n\nChallenge 3 results: ")
for book in libIter: 
    print(book)