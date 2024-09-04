from collections import OrderedDict

# Criando um OrderedDict com pares chave-valor.
# A ordem de inserção é mantida, o que significa que os itens serão armazenados e acessados na ordem em que foram adicionados.
ord_dict = OrderedDict(
    [('maçã', 10),   
     ('banana', 20), 
     ('uva', 3),     
     ('laranja', 15)] 
)

# Exibindo o dicionário ordenado inicial
print(ord_dict)

# Movendo o item 'laranja' para o início do OrderedDict.
# O parâmetro `last=False` indica que o item deve ser movido para o início (primeira posição).
ord_dict.move_to_end('laranja', last=False)

# Exibindo o dicionário após mover 'laranja' para o início
print(ord_dict)


# Verificando a diferença entre OrderedDict e dict no quesito ordenação
# Vamos criar dois OrderedDicts com a mesma chave-valor, mas em ordens diferentes

ord_dict1 = OrderedDict(
    [('maçã', 10), 
     ('banana', 20),
     ('uva', 3),
     ('laranja', 15)]
)

ord_dict2 = OrderedDict(
    [('maçã', 10), 
     ('uva', 3),
     ('banana', 20),
     ('laranja', 15)]
)

# Comparando os dois OrderedDicts. 
# A comparação leva em consideração a ordem dos itens. Portanto, como a ordem dos itens é diferente, o resultado será False.
print(ord_dict1 == ord_dict2)

# Criando dois dicionários comuns (dict) com as mesmas chaves e valores, mas em ordens diferentes

my_dict1 = {
    'maçã': 10, 
    'banana': 20,
    'uva': 3,
    'laranja': 15
}

my_dict2 = {
    'maçã': 10, 
    'uva': 3,
    'banana': 20,
    'laranja': 15
}

# Comparando os dois dicionários comuns.
# A comparação entre dicts não leva em consideração a ordem dos itens. Como as chaves e os valores são os mesmos, o resultado será True.
print(my_dict1 == my_dict2)
