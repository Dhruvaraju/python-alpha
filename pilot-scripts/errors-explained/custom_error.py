# a custom error class should extend the base Exception class or any other predefined exception
# Custom exception class is just another name for a predefined exception class
class TooManyPages(Exception):
    pass

class Book:
    def __init__(self, name, total_pages: int, pages_read: int):
        self.name = name
        self.total_pages = total_pages
        self.pages_read = pages_read
    
    def __repr__(self):
        return f"<Book {self.name}, total pages: {self.total_pages}, read: {self.pages_read}>"
    
    def read(self, pages: int) -> 'Book':
        if pages > self.total_pages or self.pages_read + pages > self.total_pages:
            raise TooManyPages(f"You are trying to read {pages} pages, but the book has only {self.total_pages} pages")
        else:
            self.pages_read += pages
            print(f"You have read {pages} pages of {self.total_pages}")

python_book = Book("Python", 100, 0)
python_book.read(10)
print(python_book.__repr__())

try:
    python_book.read(110)
except TooManyPages as e:
    print("Exception Caught: ",e)
else:
    print("Book updated successfully")
finally:
    print("Process completed")


