from abc import ABC, abstractmethod


class ItemLibrary(ABC):
    def __init__(self, title, author, price):
        self.__title = title
        self.__author = author
        self.__price = price

    @property
    def title(self):
        return self.__title
    
    @property
    def author(self):
        return self.__author
    
    @property
    def price(self):
        return self.__price

    @title.setter
    def title(self, title):
        self.__title = title
    
    @author.setter
    def author(self, author):
        self.__author = author
    
    @price.setter
    def price(self, price):
        self.__price = price

    @abstractmethod
    def apply_discount(self):
        pass    
        