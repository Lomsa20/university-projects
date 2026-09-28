class Book:
    def  __init__(self,title,author):
        self._title = title
        self._author = author
        self._available = True
    def __str__(self):
        status = 'Available' if self._available else "Borrowed"
        return f'{self._title} by {self._author}, \n available: {status}'
class Library:
    def __init__(self):
        self._books = []
    def add_book(self,book):
        self._books.append(book)
    def borrow_book(self,title):
        for book in self._books:
            if book._title == title and book._available:
                book._available = False
                return True
        return False
    def return_book(self,title):
        for book in self._books:
            if book._title == title:
                book._available = True
                return True
        return False
    def __str__(self):
        return f"Library : \n" + '\n'.join(str(book) for book in self._books)

lib = Library()
lib.add_book(Book("1984", "George Orwell"))
lib.add_book(Book("Python Basics", "John Doe"))
lib.borrow_book("1984")
print(lib)
