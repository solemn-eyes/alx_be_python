class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_checked_out = False
    def check_out(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            return True
        return False
    
    def return_book(self):
        return not self.is_checked_out
    
    def __str__(self):
        return f"{self.title} by {self.author}"

class Library:
    def __init__(self):
        self.books = []
    
    
    def add_book(self, book):
        self.books.append(book)
    def check_out_book(self, title):
        for book in self.books:
            if book.title == title and book.is_available():
                book.check_out()
                return f"Checked out: {book.title}"
            return f"Book '{title}' is not available."
    def return_book(self, title):
        for book in self.books:
            if book.title == title and not book.is_available():
                book.return_book()
                return f"Returned: {book.title}"
        return f"Book '{title}' was not checked out."
    def list_available_books(self):
        available_books = [str(book) for book in self.books if book.is_available()]
        if not available_books:
            print("No books available.")
        else:
            for book in available_books:
                print(book)

    