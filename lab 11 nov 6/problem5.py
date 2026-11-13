# Problem 5: Book and Library classes

# Part (a): Book class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_author(self):
        return self.author

    def set_author(self, author):
        self.author = author

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")

    def __str__(self):
        return f"Book(title={self.title}, author={self.author})"


# Part (b): Library class
class Library:
    def __init__(self, library_name):
        self.library_name = library_name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_catalog(self):
        if not self.books:
            print(f"{self.library_name} has no books.")
        else:
            print(f"{self.library_name} catalog:")
            for book in self.books:
                print(f" - {book.title} by {book.author}")

    def __str__(self):
        return f"Library(name={self.library_name})"


# Part (c): Demonstration
if __name__ == "__main__":
    library = Library("Westside Library")
    book1 = Book("Pride and Prejudice", "Jane Austen")
    book2 = Book("The Hobbit", "J.R.R. Tolkien")

    library.add_book(book1)
    library.add_book(book2)

    print(library)
    print(book1)
    print(book2)
    library.display_catalog()
