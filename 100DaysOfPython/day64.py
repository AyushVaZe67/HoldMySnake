class Library:
    books = []
    no_of_books = 0

    def add_book(self, book_name):
        self.__class__.books.append(book_name)
        self.__class__.no_of_books += 1

    def show_all_books(self):
        print("Books in library:", self.__class__.books)
        print("Total books:", self.__class__.no_of_books)

l1 = Library()
l1.add_book('Bible')
l1.add_book('Gita')
l1.show_all_books()
