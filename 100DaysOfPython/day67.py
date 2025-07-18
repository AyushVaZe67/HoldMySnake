class Library:
    def __init__(self):
        self.no_of_books = 0
        self.books = []

    def add_book(self,book):
        self.books.append(book)
        self.no_of_books = len(self.books)

    def show_info(self):
        print(f'{self.no_of_books} - {self.books}')


l1 = Library()
l1.add_book('Bible')
l1.show_info()
l1.add_book('Gita')
l1.show_info()
l1.add_book('Quran')
l1.show_info()
