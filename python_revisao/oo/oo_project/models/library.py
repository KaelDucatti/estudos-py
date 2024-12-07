from models import Evaluate
from models.items.item_library import ItemLibrary
from models.items.book import Book
from models.items.magazine import Magazine


class Library:
    libraries = []

    def __init__(self, name):
        self.__name = name
        self.__active = False
        self.__collection = []
        self.__evaluations = []
        Library.libraries.append(self)

    def __str__(self):
        return self.__name

    @property
    def name(self):
        return self.__name

    @property
    def active(self):
        return "Active" if self.__active else "Inactive"

    @property
    def evaluations(self):
        return self.__evaluations

    @property
    def collection(self):
        return self.__collection

    @active.setter
    def active(self, status):
        self.__active = status

    @classmethod
    def show_libraries(cls):
        print("List of libraries:")
        for lib in cls.libraries:
            print(f"Name: {lib.name.ljust(15)} | State: {lib.active}")

    def change_active_state(self):
        self.__active = not self.__active

    def add_evaluation(self, username, evaluation):
        evaluation = Evaluate(username, evaluation)
        self.evaluations.append(evaluation)

    def show_evaluations(self):
        print("\nUsers evaluations:")
        for e in self.evaluations:
            print(f"Username: {e.username.ljust(11)} | Evaluation: {e.evaluation}")

    def calculate_rating(self):
        if not self.evaluations:
            return f"{self.name} rating: No evaluations yet."

        total = sum(evaluation.evaluation for evaluation in self.evaluations)
        rating = total / len(self.evaluations)
        return f"{self.name}'s rating: {rating:.2f}"

    def add_items(self, item):
        if isinstance(item, ItemLibrary):
            self.__collection.append(item)

    def show_collection(self):
        print(f"\n{self.name}'s Collection:")
        for c in self.collection:
            if isinstance(c, Book): 
                print(
                    f"Title: {c.title}\n" 
                    f"Author: {c.author}\n" 
                    f"Price: {c.price:.2f}\n"
                    f"ISBN: {c.isbn}\n"
                )
            elif isinstance(c, Magazine):
                print(
                    f"Title: {c.title}\n" 
                    f"Author: {c.author}\n" 
                    f"Price: {c.price:.2f}\n"
                    f"Edition: {c.edition}\n"
                )
