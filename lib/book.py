#!/usr/bin/env python3
class Book:
    '''Book class'''

    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count

    def turn_page(self):
        print("Flipping the page...ye youre almost done !!")

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if not isinstance(value, int):
            print("page_count must be an integer")
        else:
            self._page_count = value

from book import Book


book = Book("wizard of oz", 272)


print("Title:", book.title)
print("Page Count:", book.page_count)

book.turn_page()

        