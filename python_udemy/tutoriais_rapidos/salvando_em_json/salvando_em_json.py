import json


person = {
    "name": "Kael",
    "surname": "o Cruel",
    "address": [
        {"street": "Estado de Israel", "number": 39},
        {"street": "Gildo de Freitas", "number": 624},
    ],
    "height": 1.73,
    "favorite_numbers": (3, 7, 33),
    "developer": True,
    "nothingess": None,
}

with open("salvando_em_json.json", "w", encoding="utf8") as file:
    json.dump(
        person, 
        file,
        indent=4,
    )

with open("salvando_em_json.json", "r", encoding="utf8") as file:
    data = json.load(file)
    print(data)

data