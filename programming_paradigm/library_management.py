class book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def __str__(self):
        return f"Book: {self.title}, Author: {self.author}"
class library:
    def __init__(self):
        self.books = []
    def add_book(self, book):
        self.books.append(book)
    def list_books(self):
        return [str(book) for book in self.books]
    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return str(book)
        return "Book not found"
    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                return f"Removed: {book.title}"
        return "Book not found"
    