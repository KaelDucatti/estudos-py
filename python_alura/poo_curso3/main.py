import json
from os import getcwd
from pathlib import Path

import requests
from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse


app = FastAPI()

dir = Path(getcwd()) / "restaurants_files"
path = dir / "McDonald’s.json"


@app.get("/api/mcdonalds")
def get_mcdonalds():
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)
        return JSONResponse(content=data)


"""
1. Faz uma requisição GET para a URL especificada e armazena o resultado na variável response.

2. Verifica se o status da resposta é 200 (OK). Se não for, imprime uma mensagem de erro com o código de status.

3. Carrega os dados JSON da resposta usando o método response.json().

4. Cria um dicionário chamado restaurant_data que irá armazenar os nomes de todas as empresas como chaves e seus dados como valores.

5. Itera sobre os itens dos dados JSON, extraindo o valor da chave "Company" e atribuindo-o à variável restaurant_name.

6. Verifica se o nome da empresa (restaurant_name) já existe no dicionário restaurant_data. Se não existir, cria uma nova entrada com uma lista vazia.

7. Cria um dicionário json_data com os dados restantes (item, preço, descrição) e adiciona esse dicionário à lista correspondente no dicionário restaurant_data.

8. Retorna os dados dos restaurantes (restaurant_data) como resposta da função.
"""
@app.get("/api/restaurants/")
def get_restaurant(restaurant: str = Query(None)):
    url = "https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        restaurant_data = []
        
        if restaurant is None:
            return {"data": data}
        
        for item in data:
            if restaurant == item["Company"]:
                json_data = {
                    "item": item["Item"],
                    "price": item["price"],
                    "description": item["description"],
                }

                restaurant_data.append(json_data)
        return {"Restaurant": restaurant, "Menu": restaurant_data}

    else:
        return {"Error": f"{response.status_code} - {response.text}"}
