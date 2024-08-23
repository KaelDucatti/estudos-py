# fazendo um looping que insere valores em uma lista até que digitar "sair"
carrinho: list = []
produto: str = ""

while produto != "sair":
    produto = input("Digite um produto: ")
    if produto != "sair":
        carrinho.append(produto)

print(carrinho)    
    