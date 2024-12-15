# diferentemente de lsitas, tuplas são imutáveis

# Verificando se todos os elementos de uma lista são pares
lista1 = (2, 4, 6, 8, 9)
if all(x % 2 == 0 for x in lista1):
    print("Todos valores pares")
else:
    print("Nem todos os valores são pares")


# verificando se nenhum valor está entre os proibidos
lista2 = (1, 2, 3, 4, 5, 6, 90)
proibidos = (11, 12, 90)

if any(x in lista2 for x in proibidos):
    print("Nem todos os valores da tupla são permitidos")
else:
    print("A tupla está ok")


    