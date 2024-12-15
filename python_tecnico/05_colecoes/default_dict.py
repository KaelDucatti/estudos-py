from collections import defaultdict


# criando um `default_dict` e utilizando uma função para definir o valor default
def valor_padrao():
    return "valor padrão"

dicionario = defaultdict(valor_padrao)
dicionario['a']
dicionario['d']
print(dicionario)


# criando um `default_dict` e utilizando uma função lambda para definir o valor default
dicionario = defaultdict(lambda: 0)
dicionario["b"]
dicionario["c"]
print(dicionario)

