# Outcome 11: Define a class with initialized attributes and working accessors.
class Book:
    def __init__(self, title, author, page_count):
        # Store this book's title, author, and page count on the instance.
        self.title = title
        self.author = author
        self.page_count = page_count

    # Each getter reads an attribute; its setter updates that attribute.
    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_author(self):
        return self.author

    def set_author(self, author):
        self.author = author

    def get_page_count(self):
        return self.page_count

    def set_page_count(self, page_count):
        self.page_count = page_count


if __name__ == "__main__":
    # Create an instance and demonstrate reading its attributes.
    book = Book("The Hobbit", "J.R.R. Tolkien", 310)
    print(book.get_title(), book.get_author(), book.get_page_count())
