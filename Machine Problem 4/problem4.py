# Challenge 4: The Database Memory (MySQL)

"""
* Create a DatabaseManager class to handle all communications with a MySQL database
* SQL first: Write the SQL create table for a books table. It should have columns for title, author, isbn, file_format.
The file_format should be allowed to be NULL for physical books.
* python class: The database manager class should have:
* An __init__ method to store database connection details (host, user, password, database name) and establish a connection
* A save book(self, book) method that takes a Book or Ebook object and inserts its data into the books table  
* A load_books(self) method that fetches all records from the books table, creates the appropriate Book or Ebook objects, and returns them in a list
"""

import mysql.connector
import time
# myDB = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="Y2WADUJjddGc3gC",
#     database="ev_library"
# )

# curser = myDB.cursor()

# curser.execute("SHOW DATABASES")
# for x in curser: 
#     print(x)

# curser.execute("CREATE DATABASE nameofdatabase")

# curser.execute("CREATE TABLE books (id INT AUTO_INCREMENT PRIMARY KEY,title VARCHAR(255) NOT NULL, author VARCHAR(255) NOT NULL, isbn VARCHAR(255) NOT NULL, file_format VARCHAR(255) NULL)")

# curser.execute("SHOW TABLES")

# for x in curser:
#     print(x)

# sql = "INSERT INTO books (title, author, isbn, file_format) VALUES (%s, %s, %s, %s)"
# val = [
#     ("The Hobbit", "J.R.R. Tolkien", "12345", None),
#     ("Dune", "Frank Herbert", "67890", "EPUB"),
#     ("1998", "George Orwell", "11223", "PDF"),
# ]
# valid_val = [v for v in val if all(v[i] for i in range(3))] # Empty string checker 

# curser.executemany(sql, valid_val)
# myDB.commit()

# print(curser.rowcount, "was inserted")

# curser.execute("SELECT * FROM books")

# result = curser.fetchall()

# for x in result:
#     print(x)

class DatabaseManager():
    def __init__(self): 
        self.myDB = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Y2WADUJjddGc3gC",
            database="ev_library"
        )

        self.curser = self.myDB.cursor()


    def save_books(self, title, author, isbn, file_format): 
        sql = "INSERT INTO books (title, author, isbn, file_format) VALUES (%s, %s, %s, %s)"
        val = [(title, author, isbn, file_format)]

        valid_val = [v for v in val if all(v[i] for i in range(3))] # Empty string checker 

        self.curser.executemany(sql, valid_val)
        self.myDB.commit()
        print(f"{len(valid_val)} Insert count")
        


    def load_books(self): 
        print("\n\nLoading Books\n")
        time.sleep(2)
        self.curser.execute("SELECT * FROM books")
        for x in self.curser.fetchall(): 
            print(x)

library = DatabaseManager()
while True: 
    print("Enter book details (or 'q' to quit):")
    title = input("Title: ")
    if title == 'q':
        break
    author = input("Author: ")
    isbn = input("ISBN: ")
    file_format = input("File Format (leave blank for physical books): ")
    library.save_books(title, author, isbn, file_format)

library.load_books()