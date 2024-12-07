from models import Library
from models.items import Book
from models.items import Magazine



lib1 = Library("Alexandria")
lib2 = Library("Saraiva")
lib3 = Library("Cultura")

book = Book(
    author="Luciano Ramalho", 
    price=100, 
    title="Python Fluente", 
    isbn=1234567890123
)
magazine = Magazine(
    author="Fulano", 
    price=30, 
    title="Super Interessante", 
    edition=10
)

book.apply_discount()

def main():
    lib1.change_active_state()

    Library.show_libraries()

    lib1.add_evaluation(username="Kael", evaluation=10)
    lib1.add_evaluation(username="Grace", evaluation=2)
    lib1.add_evaluation(username="Naju", evaluation=9.2)

    lib1.show_evaluations()

    lib1.calculate_rating()
    lib2.calculate_rating()

    lib1.add_items(book)
    lib1.add_items(magazine)

    lib1.show_collection()


if __name__ == "__main__":
    main()
