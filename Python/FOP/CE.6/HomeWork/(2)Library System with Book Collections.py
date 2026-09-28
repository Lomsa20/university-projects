class Book:
    def __init__(self, title, author):
        self.tittle = title
        self.author = author
    def __str__(self):
        return f'{self.tittle} by {self.author}'
class BookCollection:
    def __init__(self, books= None):
        self.books = books if books else []
    def __add__(self, other):
        return BookCollection(self.books + other.books)
    def display(self): #shows us every books that are in the collection
        for book in self.books:
            print(book)
    def __str__(self):
        return f"{len(self.books)}" # we use len because to count how many books are in collection
class DigitalCollection(BookCollection):
    def __init__(self, books= None):
        super().__init__(books)
    def display(self):
        print("Digital Collection")
        for i,book in enumerate(self.books, 1):
            print(f"{i}. {book.tittle.upper()}, {book.author}")
class Library:
    def __init__(self):
        self.collection = []
    def add_collection(self, collection):
        self.collection.append(collection)
    def show_all_books(self):
        for i, collection in enumerate(self.collection, 1):
            print(f"collection {i}")
            collection.display()

# Create books
b1 = Book("1984", "George Orwell")
b2 = Book("Brave New World", "Aldous Huxley")
b3 = Book("Python 101", "Michael Driscoll")
b4 = Book("Deep Learning", "Ian Goodfellow")

# Create collections
collection1 = BookCollection([b1, b2])
collection2 = DigitalCollection([b3, b4])

# Merge collections
merged = collection1 + collection2

# Library
library = Library()
library.add_collection(collection1)
library.add_collection(collection2)
library.add_collection(merged)

# Display all
library.show_all_books()

