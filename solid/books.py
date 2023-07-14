from typing import List, Union

class Book:
    def __init__(self, title: str, author: str) -> None:
        self.title = title
        self.author = author
        self.current_page = 0

    def turn_page(self, page: int) -> None:
        self.current_page = page

    def next_page(self):
        self.current_page += 1


class Library:
    def __init__(self) -> None:
        self.books: List[Book] = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def find_book(self, title: str) -> Union[Book, str]:
        try:
            return [b for b in self.books if b.title == title][0]
        except IndexError:
            return "Book does not exist"


b1 = Book("Test1", "T")
b2 = Book("Test1", "T")
b3 = Book("Test1", "T")
b4 = Book("Test1", "T")

library = Library()
library.add_book(b1)
library.add_book(b2)
library.add_book(b3)
library.add_book(b4)

print(library.find_book("Test1"))
print(library.find_book("Test1asd"))