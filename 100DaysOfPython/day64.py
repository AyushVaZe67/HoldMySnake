class Library:
    books = []
    no_of_books = 0

    def add_book(self,book_name):
        Library.books.append(book_name)
        self.no_of_books += 1

    def show_all_books(self):
        print(self.books)

l1 = Library()
l1.add_book('Bible')
l1.add_book('Gita')
l1.show_all_books()