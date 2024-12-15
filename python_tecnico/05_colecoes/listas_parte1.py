my_list = [10, 2, 43, 4, 12, 85, 199, 3, 6, 95]
print(my_list)


# ordenando lista
ordered_list = sorted(my_list)
print(ordered_list)

# adicionando valores na minha lista
ordered_list.append(1)
print(ordered_list)

# adicinando múltiplos valores à lista
more_elements = [2, 3, 4, 5, 6]
ordered_list.extend(more_elements)
print(ordered_list)

# inserindo elementos em uma posição específica da lista
ordered_list.insert(0, 100)
print(ordered_list)

# removendo primeira ocorrência de uma elemento na lista
ordered_list.remove(2)
print(ordered_list)

# removendo e retornando um valor pelo seu index
removed_value = ordered_list.pop(0)
print(ordered_list)
print(removed_value)

# removendo todos os elementos de uma lista
ordered_list.clear()
print(ordered_list)

# revertendo uma lista
print(my_list)
my_list.reverse()
print(my_list)
# podemos fazer o mesmo com...
print(my_list[::-1])

# acessando elementos pela posição 
element = my_list[0]
print(element)

# acessando elementos por intervalo
interval = my_list[1:5]
print(interval)

# contando número de elementos presentes na lista
list_size = len(my_list)
print(list_size)

# retornando maior elemento presente na lista
major = max(my_list)
print(major)

# retornando menor elementos presenta na lista
minor = min(my_list)
print(minor)

# soma de todos os elementos da lista
summarize = sum(my_list)
print(summarize)

# retornando o número de ocorrências de um valor na lista
element_count = my_list.count(2)
print(element_count)

# retornando o index da primeira ocorrência de uma valor
index = my_list.index(85)
print(index)


