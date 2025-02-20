from pathlib import Path
from json import dump, load
from os import getcwd


path = Path(getcwd()) / "oo"

class Person:
    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age

    def dump_data(self):
        file_path = path / f"{self.name}.json"
        with open(file_path, "w") as file:
            dump(self.__dict__, file, indent=4)
            return
        
    def load_data(self, file_path):
        with open(file_path, "r") as file:
            data = load(file)
            self.name = data["name"]
            self.age = data["age"]
            return
        
def main():
    kael = Person()
    kael.load_data(path / "Kael.json")
    print(kael.__dict__)

    naju = Person()
    naju.load_data(path / "Naju.json")
    print(naju.__dict__)

if __name__ == "__main__":
    main()
    
