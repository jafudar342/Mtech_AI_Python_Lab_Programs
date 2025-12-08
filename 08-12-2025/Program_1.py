class Book:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        self.books.append((title, author))
        print("Books added successfully")

    def drop_book(self, title):
        for b in self.books:
            if b[0] == title:
                self.books.remove(b)
                print("Book removed successfully")
                return
        print("Book not found!!")

    def display(self):
        print("Books list: ")
        for b in self.books:
            print("Title: ", b[0], " | Author: ", b[1])
        print()


obj = Book()

obj.add_book("Harry Potter", "J.K. Rowling")
obj.add_book("The Alchemist", "Paulo Coelho")

obj.display()

obj.drop_book("Harry Potter")

obj.display()
