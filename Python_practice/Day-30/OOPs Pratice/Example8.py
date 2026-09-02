"""Question 8: Class with String Representation
Question: Define a class Book with attributes title and author. Override the __str__ method to print the book details.
"""

class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author

    def __str__(self):
        return f"Title:{self.title}, Author :{self.author}"

title=input("Enter the book title: ")
author=input("Enter the book author: ")
book=Book(title,author)
print(book)