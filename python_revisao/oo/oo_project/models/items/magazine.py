from models.items.item_library import ItemLibrary


class Magazine(ItemLibrary):
    def __init__(self, title, author, price, edition):
        super().__init__(title, author, price)
        self.__edition = edition

    @property
    def edition(self):
        return self.__edition
    
    @edition.setter
    def edition(self, edition):
        self.__edition = edition 

    def apply_discount(self):
        self.price -= (self.price * 0.05)
