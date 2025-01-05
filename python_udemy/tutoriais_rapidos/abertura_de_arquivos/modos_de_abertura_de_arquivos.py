from hmac import new
import os
from pathlib import Path


path = Path(__file__).parent 
file_path = path / "text.txt"

with open(file_path, "w+", encoding="utf8") as file:
    file.write("Kael\n")
    file.write("Naju\n")
    file.write("Grace\n")
    file.seek(0)
    print(file.read())

with open(file_path, "r+") as file: 
    file.seek(0, 2)
    file.write("Nina\n")
    file.seek(0)
    print(file.read())

with open(file_path, "a+") as file:
    file.write("Hades\n")
    file.seek(0)
    print(file.read())

with open(file_path, "a") as file:
    file.writelines(
        ("Sky\n", "Morango\n", "Pown pown\n")
    )

with open(file_path, "r") as file:
    print(file.read())

with open(file_path, "r") as file:
    print(file.readline(), end="")
    print(file.readline(), end="")
    print(file.readline(), end="")

old_file_name = path / "text.txt"
new_file_name = path / "file.txt"

os.rename("file.txt", "gatos.txt")
os.remove(file_path)
