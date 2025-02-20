import json
import requests
from pathlib import Path


url = "https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json"

response = requests.get(url)

if response.status_code == 200:
    json_data = response.json()
    restaurant_data = {}

    for item in json_data:
        restaurant_name = item["Company"]

        if restaurant_name not in restaurant_data:
            restaurant_data[restaurant_name] = []

        data = {
            "item": item["Item"],
            "price": item["price"],
            "description": item["description"],
        }
        restaurant_data[restaurant_name].append(data)
else:
    print(f"Error: {response.status_code}")


output_dir = Path(__file__).parent / "restaurants_files"
output_dir.mkdir(parents=True, exist_ok=True)

for restaurant_name, data in restaurant_data.items():
    path = output_dir / f"{restaurant_name}.json"

    with open(path, "w", encoding="utf-8") as file:
        json.dump(
            obj=data,
            fp=file,
            indent=4,
        )
