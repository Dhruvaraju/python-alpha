from tokenize import String


class Book:
    type = "Hardcover", "Paperback"
    def __init__(self, title: String, type: String, author: String):
        self.title = title
        self.type = type
        self.author = author

    def instance_method(self):
        print("Instance method called")
        return(f"Title: {self.title} is a {self.type} book authored by {self.author}")

    @classmethod
    def class_method(cls) -> String:
        return ("Class method called")
    
    @classmethod
    def hardcover(cls, title: String, author: String) -> 'Book':
        return (f"Book {title} by {author} is a {cls.type[0]} book")
    
    @classmethod
    def paperback(cls, title, author):
        return (f"Book {title} by {author} is a {cls.type[1]} book")

    @staticmethod
    def static_method():
        return ("Static method called")

    def __repr__(self):
        return (f"<Book {self.title} {self.type} {self.author} >")

# To call an instance method we need to create an instance of the class
# and then call the instance method
book = Book("Python", "Hardcover", "Guido van Rossum")
print(book.__repr__())
print(book.instance_method())

# to call a static or class method we can call the class directly no need of creating an instance
print(Book.class_method())
print(Book.static_method())

# We can call hardcover and paperback methods without passing the type of book
hardcover = Book.hardcover("Trojan Horse", "Mark Russanovich")
paperback = Book.paperback("Black Hawk Down", "Jack")
print(hardcover)
print(paperback)