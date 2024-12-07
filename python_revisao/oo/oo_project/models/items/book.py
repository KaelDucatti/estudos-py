from models.items.item_library import ItemLibrary


class Book(ItemLibrary):
    def __init__(self, title, author, price, isbn):
        super().__init__(title, author, price)
        self.__isbn = isbn

    @property
    def isbn(self):
        return self.__isbn
    
    @isbn.setter
    def isbn(self, isbn):
        self.__isbn = isbn

    def apply_discount(self):
        self.price -= (self.price * 0.10)
    