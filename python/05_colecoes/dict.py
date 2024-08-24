meu_dict = {
    "a": [10, 20, 30],
    "b": (40, 50, 60),
    "c": {7: 0, 8: 0, 9: 0}
}

# adicionando valores à lista dentro do dicionário
meu_dict["a"].extend(["a", 1])
print(meu_dict)

# adicionando valores à tupla dentro do dicionário
meu_dict["b"] = meu_dict["b"] + ("b", 2,)
print(meu_dict)

# adicionando valores ao dicionário dentro do dicionário
meu_dict["c"][10] = 0
print(meu_dict)


