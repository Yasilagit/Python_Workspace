from abc import ABC, abstractmethod


class Book(ABC):

    @abstractmethod
    def display(self):
        pass


class MyBook(Book):
    def __init__(self, title, authour, price):
        self.title = title
        self.authour = authour
        self.price = price

    def display(self):
        print("Title: " + self.title)
        print("Author: " + self.authour)
        print("Price: " + str(self.price))


title = input()
authour = input()
price = input()

myBook = MyBook(title, authour, price)
myBook.display()
